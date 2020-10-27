from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

    def contratarLineas(self, numeroLineas):
        return self.price * numeroLineas
