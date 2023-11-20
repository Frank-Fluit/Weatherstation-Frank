from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
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