from django.shortcuts import render
from django.http import HttpResponse


def web (request):
    return HttpResponse("Pagina principal ")

def espacios (request):
    return HttpResponse("Pagina de los espacios de simulacion")

def simulacion (request):
    return HttpResponse("Pagina de las simulaciones")