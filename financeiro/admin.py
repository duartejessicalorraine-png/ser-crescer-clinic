from django.contrib import admin
from .models import ServiceType, Invoice, Payment

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "default_price", "duration_minutes", "active")
    list_filter = ("active",)
    search_fields = ("name",)

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "patient_name", "due_date", "total_amount", "status", "created_at")
    list_filter = ("status", "due_date")
    search_fields = ("patient_name", "responsible_name", "responsible_whatsapp")
    inlines = [PaymentInline]


