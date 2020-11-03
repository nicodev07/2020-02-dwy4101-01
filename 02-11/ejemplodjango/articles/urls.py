from django.contrib import admin
from django.urls import path, include
from .models import Article
from rest_framework import routers, serializers, viewsets

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['title','description','user']

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

router = routers.DefaultRouter()
router.register(r'',ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
