from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse,JsonResponse

"""
Petición HTTP.
1. Request: Solicitud del cliente al servidor
2. Response: La respuesta del servidor al cliente
"""

def holaMundo(request):
    message = 'Hola {name}. Bienvenido. Tienes {age} años'.format(
        name=str(request.GET['name']),
        age=str(request.GET['age'])
        )
    return HttpResponse(message)

def holaMundoJson(request):

    age = request.GET['age']

    """
    request.GET['age'] es un string, por ende, debo parsearlo a un int para validar los años de la persona
    que lo va a enviar mediante query param.
    """

    if int(age) < 18:
        return JsonResponse({'message': 'No tienes acceso'})

    message = 'Hola {name}. Bienvenido. Tienes {age} años'.format(
        name=str(request.GET['name']),
        age=str(age)
        )
    return JsonResponse({'message': message})


def holaMundoFeo(request):
    message = None
    if int(request.GET['age']) < 18:
        message = 'No tienes permisos'
    else:
        message = 'Hola ',str(request.GET['name']),'. Bienvenido. Tienes',str(request.GET['age']),' años'
    
    return JsonResponse({'message': message})

def holaMundoUsuario(request, name, age):
    message = 'Hola {name} bienvenido. Tienes {age} años'.format(
        name=name,
        age=age
    )
    return JsonResponse({'message': message})

def holaMundoUsuarioSolo(request, name):
    message = 'Hola {name} bienvenido'.format(
        name=name
    )
    return JsonResponse({'message': message})  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('planes/', include('planes.urls')),
    path('hola-mundo', holaMundo),
    path('hola-mundo-json', holaMundoJson),
    path('hola-usuario/<str:name>', holaMundoUsuarioSolo),
    path('hola-usuario/<str:name>/<int:age>', holaMundoUsuario)
]
