from django.urls import path
from . import views



#URLConfiguration, every apps needs it and has to be added to the main configuration folder
urlpatterns = [
    path('hello/', views.say_hello)
]