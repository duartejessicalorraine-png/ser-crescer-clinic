from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "professional", "start_at", "end_at", "title")
    search_fields = ("patient__full_name", "professional__username", "title")
    list_filter = ("professional", "start_at")
    ordering = ("-start_at",)


