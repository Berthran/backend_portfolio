from django.shortcuts import render

from django.http import HttpResponse

from .models import Menu



def index(request):
    return HttpResponse("Hello, world. This is the index view of Demoapp.")
