from django.urls import path
from django.http import Http404
from django.shortcuts import render
from .models import Plan

""" Este es el controlador para /planes/ """


def index(request):
    planes = Plan.objects.order_by('name')[:5]
    return render(request, 'planes/index.html', {'planes': planes})


""" Este es el controlador para /planes/{id}.
NOTA: Está declarado como {id} porque es PARAMETRIZABLE. """


def show(request, planId):
    try:
        plan = Plan.objects.get(pk=planId)
        numeroLineas = int(request.GET['numeroLineas'])
        preciosPorLineas = plan.contratarLineas(numeroLineas)

    except Plan.DoesNotExist:
        raise Http404('El plan no existe')
    
    return render(request, 'planes/show.html', {
        'plan': plan,
        'preciosPorLineas': preciosPorLineas,
        'numeroLineas': numeroLineas
    })


urlpatterns = [
    # ej: /planes/
    path('', index),
    # ej: /planes/1
    path('<int:planId>', show)
]
