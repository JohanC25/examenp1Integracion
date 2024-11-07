# facturacion/forms.py
from django import forms
from .models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['proveedor', 'numero_factura', 'fecha_emision', 'monto_total', 'descripcion']
