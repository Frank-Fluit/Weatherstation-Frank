from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dataprocessing.models import Temperature, WindSpeed, Location
from domainlogic.AnalysisService import AnalysisService
from django.http import JsonResponse



import pandas as pd


def index(request):
    return HttpResponse("Hello, world. You're at the dataprocessing index.")


@csrf_exempt
def say_hello(request):
    data = {'message': 'Hello from the say_hello endpoint in the dataprocessing unit!'}
    return JsonResponse(data)





@csrf_exempt
def csv_processing(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        results = AnalysisService.analyze_csv(csv_file)
        print("we are in the view right now")
        return JsonResponse(results)

    return HttpResponse("Upload CSV File")

@csrf_exempt
def data_post(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        wind_temp_df = AnalysisService.prepare_for_database(csv_file)
        print("We are in the data_post view now")
        print(wind_temp_df)

        for index, row in wind_temp_df.iterrows():
            # Access individual values using column names
            name = row['name']
            datetime = row['datetime']
            temp = row['temp']
            windspeed = row['windspeed']

            location_instance, created = Location.objects.get_or_create(location=name)
            print(location_instance)

            windspeed_instance = WindSpeed(location=location_instance,windspeed=windspeed,timestamp=datetime)
            windspeed_instance.save()
            print(windspeed_instance)

            temperature_instance = Temperature(location=location_instance,temperature=temp,timestamp=datetime)
            temperature_instance.save()
            print(temperature_instance)

        return HttpResponse("Your data has been uploaded")

    return HttpResponse("Upload CSV File")