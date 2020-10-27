from django.urls import path, include
from django.http import Http404
from django.shortcuts import render
from .models import Plan
from rest_framework import routers, serializers, viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
# Serializers define the API representation.
class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['name', 'id']

# ViewSets define the view behavior.
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['name', 'id']
    search_fields = ['name', 'id']
    serializer_class = PlanSerializer

router = routers.DefaultRouter()
router.register(r'', PlanViewSet)
urlpatterns = [
     path('', include(router.urls)),
]
