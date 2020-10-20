from django.urls import path
from django.http import HttpResponse,JsonResponse

def holaDesdePlanes(request):
    return HttpResponse('Hola!')
    
urlpatterns = [
    path('', holaDesdePlanes)
]