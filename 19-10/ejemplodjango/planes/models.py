from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=120)