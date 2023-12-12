from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.say_hello, name="hello"),
    path('csv/', views.csv_processing, name="csv_processing"),
    path("", views.index, name="index"),
    path('datapost/', views.data_post, name="data_post"),
    path('compare/', views.compare, name="compare"),
    path('correlation/', views.correlation, name="correlation"),
    path('test_api/', views.test_api, name="test_api"),
    # path("get_loc_based_on_lat_lon/", views.get_loc_based_on_lat_lon, name="get_loc_based_on_lat_lon"),
    path("get_weather_based_on_loc/", views.get_weather_based_on_loc, name="get_weather_based_on_loc"),
    path("get_weather_based_on_lat_lon/", views.get_weather_based_on_lat_lon, name="get_weather_based_on_lat_lon")
]
