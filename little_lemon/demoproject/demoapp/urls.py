# Configuring a urls.py file in the app folder
from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name="index"),
        ]
