from django.db import models


class Cliente(models.Model):
    nombre      = models.CharField(max_length=200)
    apellidos   = models.CharField(max_length=200)
    status      = models.BooleanField(default=True)
    
    def __unicode__(self):
        return "%s, %s" % (self.apellidos.upper(), self.nombre)

    
class Producto(models.Model):
    nombre      = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    status      = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.nombre
