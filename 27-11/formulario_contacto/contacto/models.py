from django.db import models

class Contacto(models.Model):
    titulo = models.CharField(max_length=100)
    mensaje = models.TextField()
    receptor = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)