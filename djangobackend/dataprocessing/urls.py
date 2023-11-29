from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.say_hello, name="hello"),
    path('csv/', views.csv_processing, name="csv_processing"),
    path("", views.index, name="index"),
    path('datapost/', views.data_post, name="data_post"),
    path('compare/', views.compare, name="compare"),
    path('correlation/', views.correlation, name="correlation")
]
