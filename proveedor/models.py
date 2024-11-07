from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    productos = models.TextField()
    condiciones_comerciales = models.TextField()

    def __str__(self):
        return self.nombre
