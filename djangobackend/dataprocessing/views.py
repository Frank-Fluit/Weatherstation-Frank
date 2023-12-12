from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataprocessing.models import Temperature, WindSpeed, Location
#from domainlogic.AnalysisService import AnalysisService
from django.db.models import Avg

# dataprocessing/views.py
from domainlogic.AnalysisService import AnalysisService
import requests
import json

import pandas as pd



class WeatherDTO:
    def __init__(self, temperature, city_name):
        self.temperature = temperature
        self.city_name = city_name



def index(request):
    return HttpResponse("Hello, world. You're at the dataprocessing index.")


@csrf_exempt
def say_hello(request):
    data = {'message': 'Hello from the say_hello endpoint in the dataprocessing unit!'}
    return JsonResponse(data)


@csrf_exempt
def compare(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):

        csv_file = request.FILES['csv_file']
        results_analyzer_input = AnalysisService.analyze_csv(csv_file)

        print(results_analyzer_input)

        avg_windspeed_overall = WindSpeed.objects.aggregate(avg_windspeed_overall=Avg('windspeed'))['avg_windspeed_overall']
        avg_temperature_overall = Temperature.objects.aggregate(avg_temperature_overall = Avg('temperature'))['avg_temperature_overall']

        avg_temperature_user = results_analyzer_input["average_temp"]
        avg_windspeed_user = results_analyzer_input["average_windspeed"]

        temperature_dif = avg_temperature_user - avg_temperature_overall
        windspeed_dif = avg_windspeed_user - avg_windspeed_overall

        results = {
            "input_avg_temp": avg_temperature_user,
            "overall_avg_temp": avg_temperature_overall,
            "temp_diff": temperature_dif,
            "input_avg_windspeed": avg_windspeed_user,
            "overall_avg_windspeed": avg_windspeed_overall,
            "temp_windspeed": windspeed_dif
        }


        return JsonResponse(results)
    return HttpResponse("Upload CSV File")


@csrf_exempt
def csv_processing(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        results = AnalysisService.analyze_csv(csv_file)
        return JsonResponse(results)

    return HttpResponse("Upload CSV File")

@csrf_exempt
def correlation(request):
    if request.method == 'POST' and request.FILES.get('csv_file1'):
        csv_file1 = request.FILES['csv_file1']
        csv_file2 = request.FILES['csv_file2']
        results = AnalysisService.correlation_temp(csv_file1, csv_file2)
        return JsonResponse(results)

    return HttpResponse("Upload CSV File")


@csrf_exempt
def data_post(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        wind_temp_df = AnalysisService.prepare_for_database(csv_file)

        for index, row in wind_temp_df.iterrows():

            name = row['name']
            datetime = row['datetime']
            temp = row['temp']
            windspeed = row['windspeed']

            location_instance, created = Location.objects.get_or_create(location=name)

            windspeed_instance = WindSpeed(location=location_instance, windspeed=windspeed, timestamp=datetime)
            windspeed_instance.save()

            temperature_instance = Temperature(location=location_instance, temperature=temp, timestamp=datetime)
            temperature_instance.save()


        return HttpResponse("Your data has been uploaded")

    return HttpResponse("Upload CSV File")

@csrf_exempt
def test_api(request):
    response = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=4d0a42399d252a0866c7c68630ad09ae').json()
    print(response)
    return JsonResponse(response, safe = False)

# @csrf_exempt
# def get_loc_based_on_lat_lon(request):
#     print("##")
#     locations_api_response = requests.get('http://api.openweathermap.org/geo/1.0/reverse?lat=52.14697&lon=5.87769&limit=5&appid=4d0a42399d252a0866c7c68630ad09ae').json()
#     print(locations_api_response)
#     print("##")
#     return JsonResponse(locations_api_response, safe = False)


# parametrise! + preprocess data + add requesting in frontend + maybe separate application
@csrf_exempt
def get_weather_based_on_loc(request):
    data = json.loads(request.body.decode('utf-8'))
    city = data.get("city")
    countryCode = data.get("countryCode")

    print("------------------------------------------------------")
    print(f"City: {city}, countryCode: {countryCode}")
    print("------------------------------------------------------")
    location = "Rotterdam"
    country = "nl"

    locations_api_response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+","+countryCode+"&APPID=4d0a42399d252a0866c7c68630ad09ae").json()
    temperature = locations_api_response.get('main', {}).get('temp')
    city_name = locations_api_response.get('name')

    weather_dto = WeatherDTO(temperature=temperature - 272.15, city_name=city_name)
    serialized_data = json.dumps({'temperature': weather_dto.temperature, 'city_name': weather_dto.city_name})
    print("##")
    return JsonResponse(serialized_data, safe=False)

#parametrise + preprocess the data
@csrf_exempt
def get_weather_based_on_lat_lon(request):
    print("-----------------------------")

    data = json.loads(request.body.decode('utf-8'))

    # Access the latitude and longitude
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Use the latitude and longitude as needed
    print("-----------------------------")
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    print("-----------------------------")
    print("##############################")

    latitude = str(latitude)
    longitude = str(longitude)
    locations_api_response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+latitude+"&lon="+longitude+"&appid=4d0a42399d252a0866c7c68630ad09ae").json()


    temperature = locations_api_response.get('main', {}).get('temp')
    city_name = locations_api_response.get('name')
    print("-----------------------------")
    print(f"Temperature: {temperature}, City: {city_name}")
    print("-----------------------------")

    weather_dto = WeatherDTO(temperature=temperature-272.15, city_name=city_name)
    # Serialize the WeatherDTO object to JSON
    serialized_data = json.dumps({'temperature': weather_dto.temperature, 'city_name': weather_dto.city_name})

    # Return the JSON response
    return JsonResponse(serialized_data, safe=False)

