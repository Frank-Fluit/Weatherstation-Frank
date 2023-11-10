from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# request handlers, weird name huh

@csrf_exempt
def say_hello(request):
    data = {'message': 'Hello from the server!'}
    return JsonResponse(data)

## After this this view has to be mapped to a url -> urls.py (name does not matter, but 
# is convention)
