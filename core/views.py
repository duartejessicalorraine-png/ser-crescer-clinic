from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Ser & Crescer Clinic - Sistema ativo")

from django.contrib.auth.models import User
from django.http import HttpResponse

def criar_admin_temporario(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@sercrescer.com",
            password="admin123"
        )
        return HttpResponse("Superusuário criado com sucesso.")
    return HttpResponse("Superusuário já existe.")
