from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "birth_date", "guardian_name", "guardian_phone", "created_at")
    search_fields = ("full_name", "guardian_name", "guardian_phone")
    list_filter = ("created_at",)


