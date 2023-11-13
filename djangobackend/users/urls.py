from django.urls import path
from . import views
from .views import UserRegistrationView


#URLConfiguration, every apps needs it and has to be added to the main configuration folder
urlpatterns = [
    path('hello/', views.say_hello), 
    path('register/', UserRegistrationView.as_view(), name='user-registration')
]