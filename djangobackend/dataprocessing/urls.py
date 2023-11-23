from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('csv/', views.csv_processing),
    path("", views.index, name="index"),
    path('datapost/', views.data_post)
]
