from django.shortcuts import render
from django.http import HttpResponse
from alumnos import controller


def index(request):
    _result = controller.GetAlumnos()
    return render(request, "alumnos/index.html", 
    {'title': _result})