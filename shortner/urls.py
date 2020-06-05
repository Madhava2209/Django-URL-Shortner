from django.contrib import admin
from django.urls import path
from shortner.views import *

urlpatterns = [
    
    path("home/",home),
    path("dashboard/",dashboard),
    path("create_short_url/",create_short_url),
    path("<str:hashcode>/",redirect_to_long_url),
    
]