from django.contrib import admin
from .models import SessionNote


@admin.register(SessionNote)
class SessionNoteAdmin(admin.ModelAdmin):
    list_display = ("patient", "professional", "session_date")
    search_fields = ("patient__full_name", "professional__username")
    list_filter = ("professional", "session_date")
    ordering = ("-session_date", "-id")


