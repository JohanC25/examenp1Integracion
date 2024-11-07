# facturacion/models.py
from django.db import models
from proveedor.models import Proveedor

class Factura(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='facturas')
    numero_factura = models.CharField(max_length=100, unique=True)
    fecha_emision = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'facturacion_factura'  # Nombre de la tabla con el prefijo
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return f"{self.numero_factura} - {self.proveedor.nombre}"
