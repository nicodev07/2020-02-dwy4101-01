from django.urls import path, include
from .models import Plan
from rest_framework import routers, serializers, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

# Encargado de serializar los datos que llegan.
class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['id','name','price']

# Encargado de ejecutar la query y "serializar" en una clase.
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    # SELECT * FROM plan WHERE name = 'Plan M'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id','name']
    # SELECT * FROM plan WHERE name LIKE '%Plan%'
    search_fields = ['id','name']
    serializer_class = PlanSerializer

# Registrar las rutas para construir una API Rest Full.
router = routers.DefaultRouter()
router.register(r'', PlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
