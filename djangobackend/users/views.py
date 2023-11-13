from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer


# should potentially add the csrf exempt option here
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


# Create your views here.

# request handlers, weird name huh

@csrf_exempt
def say_hello(request):
    data = {'message': 'Hello from the server!'}
    return JsonResponse(data)

## After this this view has to be mapped to a url -> urls.py (name does not matter, but 
# is convention)

# View for user registration is performed here

