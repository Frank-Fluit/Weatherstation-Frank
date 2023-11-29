from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dataprocessing.models import Temperature, WindSpeed, Location
from domainlogic.AnalysisService import AnalysisService
from django.db.models import Avg

import pandas as pd


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

        avg_windspeed_overall = WindSpeed.objects.aggregate(avg_windspeed_overall=Avg('windspeed'))['avg_windspeed_overall']
        avg_temperature_overall = Temperature.objects.aggregate(avg_temperature_overall = Avg('temperature'))['avg_temperature_overall']

        avg_temperature_user = results_analyzer_input["average_temp"]["temp"]
        avg_windspeed_user = results_analyzer_input["average_windspeed"]["windspeed"]

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
