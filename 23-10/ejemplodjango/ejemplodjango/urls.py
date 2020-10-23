from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse,JsonResponse

"""
Petición HTTP.
1. Request: Solicitud del cliente al servidor
2. Response: La respuesta del servidor al cliente
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('planes/', include('planes.urls')),
]
