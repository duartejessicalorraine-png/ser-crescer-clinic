from django.urls import path
from . import views

app_name = "financeiro"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("faturas/", views.invoice_list, name="invoice_list"),
]

