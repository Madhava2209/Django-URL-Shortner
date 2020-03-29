from django.contrib import admin
from django.urls import path
from authentication.views import *

urlpatterns = [
    path("signup/",signup),
    path("login/",signin),
    path("logout/",signout),
]
