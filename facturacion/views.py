# facturacion/views.py
import csv
import os
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, View
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Factura
from .forms import FacturaForm
from proveedor.models import Proveedor

# Vista para listar facturas
class FacturaListView(ListView):
    model = Factura
    template_name = 'facturacion/factura_list.html'
    context_object_name = 'facturas'

# Vista para crear una nueva factura
class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'facturacion/factura_form.html'

    def get_success_url(self):
        return reverse_lazy('factura_list')

# Vista para actualizar una factura existente
class FacturaUpdateView(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'facturacion/factura_form.html'

    def get_success_url(self):
        return reverse_lazy('factura_list')

# Vista para eliminar una factura
class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = 'facturacion/factura_confirm_delete.html'
    success_url = reverse_lazy('factura_list')

# Vista para ver los detalles de una factura
class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'facturacion/factura_detail.html'
    context_object_name = 'factura'

# Vista para mostrar la vista previa del CSV
class VistaPreviaCSVView(TemplateView):
    template_name = 'facturacion/vista_previa_csv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        csv_path = os.path.join(settings.BASE_DIR, 'Compartidos', 'proveedores.csv')

        # Verificar que el archivo existe
        if not os.path.exists(csv_path):
            context['csv_data'] = None
            messages.error(self.request, "No se encontró el archivo CSV en la carpeta 'Compartidos'.")
            return context

        # Leer el archivo CSV y agregar los datos al contexto
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            csv_data = [row for row in reader]

        context['csv_data'] = csv_data
        return context

# Vista para cargar los datos del CSV en la base de datos
class CargarCSVView(View):
    def post(self, request, *args, **kwargs):
        csv_path = os.path.join(settings.BASE_DIR, 'Compartidos', 'proveedores.csv')

        # Verificar que el archivo existe
        if not os.path.exists(csv_path):
            messages.error(request, "No se encontró el archivo CSV en la carpeta 'Compartidos'.")
            return redirect('vista_previa_csv')

        # Leer el archivo CSV y cargar los datos en la base de datos
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                proveedor_nombre = row.get('Nombre')
                proveedor, created = Proveedor.objects.get_or_create(nombre=proveedor_nombre)

                Factura.objects.get_or_create(
                    proveedor=proveedor,
                    numero_factura=row.get('Número de Factura'),
                    fecha_emision=row.get('Fecha de Emisión'),
                    monto_total=row.get('Monto Total'),
                    descripcion=row.get('Descripción', '')
                )

        messages.success(request, "Las facturas se cargaron correctamente desde el archivo CSV.")
        return redirect('factura_list')