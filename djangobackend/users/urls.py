from django.urls import path
from . import views
from .views import UserRegistrationView


urlpatterns = [
    path('hello/', views.say_hello), 
    path('register/', UserRegistrationView.as_view(), name='user-registration')
]