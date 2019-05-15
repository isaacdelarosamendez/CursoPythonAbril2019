from django.shortcuts import render
from django.http import HttpResponse
from alumnos import controller
from .models import Alumnos
from django.http import JsonResponse

def index(request):
    _result = controller.GetAlumnos()
    return render(request, "alumnos/index.html", 
    {'alumnos': _result})