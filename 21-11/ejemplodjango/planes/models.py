from django.db import models


class Plan(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    internet = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    
    def generarDescuento(self):
        if (self.price <= 10000):
            return 0.05
        if (self.price <= 11000):
            return 0.1
        if (self.price <= 13000):
            return 0.2
        if (self.price <= 15000):
            return 0.4
        if (self.price <= 20000):
            return 0.5
        
        return 0.6
    
    def calcularPrecioFinal(self):
        return self.price * (1.0-self.generarDescuento())
        