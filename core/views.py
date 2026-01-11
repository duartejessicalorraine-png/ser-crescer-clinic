from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Ser & Crescer Clinic - Sistema ativo")
