from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return redirect("/admin/")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("patients/", include("patients.urls")),
    path("records/", include("records.urls")),
    path("schedule/", include("schedule.urls")),
    path("documents/", include("documents.urls")),
    path("financeiro/", include("financeiro.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from core.views import criar_admin_temporario

urlpatterns += [
    path("criar-admin/", criar_admin_temporario),
]









