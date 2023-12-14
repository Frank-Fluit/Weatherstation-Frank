from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataprocessing.dtos import WeatherDTO
from dataprocessing.models import Temperature, WindSpeed, Location
from django.db.models import Avg

from dataprocessing.services import *
from domainlogic.AnalysisService import AnalysisService
import requests
import json
import datetime


API_KEY = "4d0a42399d252a0866c7c68630ad09ae"
API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

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

        avg_windspeed_overall = WindSpeed.objects.aggregate(
            avg_windspeed_overall=Avg('windspeed'))['avg_windspeed_overall']
        avg_temperature_overall = Temperature.objects.aggregate(
            avg_temperature_overall=Avg('temperature'))['avg_temperature_overall']

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

            windspeed_instance = WindSpeed(location=location_instance,
                                           windspeed=windspeed, timestamp=datetime)
            windspeed_instance.save()

            temperature_instance = Temperature(location=location_instance,
                                               temperature=temp, timestamp=datetime)
            temperature_instance.save()

        return HttpResponse("Your data has been uploaded")

    return HttpResponse("Upload CSV File")


@csrf_exempt
def test_api(request):
    response = requests.get(
        'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=' + API_KEY).json()
    print(response)
    return JsonResponse(response, safe=False)



@csrf_exempt
def get_weather_based_on_loc(request):

    try:
        data = json.loads(request.body.decode('utf-8'))
        city = data.get("city")
        country_code = data.get("countryCode")

        locations_api_response = get_data_ex_api_loc(city, country_code)

        temperature = locations_api_response.get('main', {}).get('temp')
        if temperature is None:
            return JsonResponse({'error': 'Temperature data not available'}, status=500)

        city_name = locations_api_response.get('name')

        weather_dto = WeatherDTO(temperature=round(temperature - 272.15, 2), city_name=city_name)
        serialized_data = json.dumps({'temperature': weather_dto.temperature, 'city_name': weather_dto.city_name})

        return JsonResponse(serialized_data, safe=False)

    except requests.RequestException as e:

        return JsonResponse({'error': str(e)}, status=500)



@csrf_exempt
def get_weather_based_on_lat_lon(request):

    try:
        data = json.loads(request.body.decode('utf-8'))

        latitude = str(data.get('latitude'))
        longitude = str(data.get('longitude'))

        api_data = get_weather_data_by_lat_lon(latitude, longitude)


        temperature = api_data.get('main', {}).get('temp')
        if temperature is None:
            return JsonResponse({'error': 'Temperature data not available'}, status=500)

        city_name = api_data.get('name')

        weather_dto = WeatherDTO(temperature=round(temperature - 272.15, 2), city_name=city_name)
        serialized_data = json.dumps({'temperature': weather_dto.temperature,
                                      'city_name': weather_dto.city_name})

        return JsonResponse(serialized_data, safe=False)

    except (json.JSONDecodeError, requests.RequestException) as e:
        return JsonResponse({'error': str(e)}, status=500)





@csrf_exempt
def get_weather_pred_loc(request):
    data = json.loads(request.body.decode('utf-8'))
    city = data.get("city")
    country_code = data.get("countryCode")

    latitude, longitude = get_lat_lon_based_loc(city,country_code)

    api_data = get_ex_api_lat_lon_pred(latitude,longitude)

    return JsonResponse(api_data, safe=False)



@csrf_exempt
def get_prediciton_based_on_lat_lon(request):

    try:
        data = json.loads(request.body.decode('utf-8'))

        latitude = str(data.get('latitude'))
        longitude = str(data.get('longitude'))

        api_data = get_ex_api_lat_lon_pred(latitude, longitude)

        return JsonResponse(api_data, safe=False)

    except (json.JSONDecodeError, requests.RequestException) as e:
        return JsonResponse({'error': str(e)}, status=500)




