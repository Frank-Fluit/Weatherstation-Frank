from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, world. You're at the dataprocessing index.")


@csrf_exempt
def say_hello(request):
    data = {'message': 'Hello from the say_hello endpoint in the dataprocessing unit!'}
    return JsonResponse(data)


@csrf_exempt
def csv_processing(request):
    data = {'message': 'Hello from the first analyses endpoint for csvs!'}
    return JsonResponse(data)
