from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.http import HttpResponse
from django.utils import timezone
import csv
import os

from .models import Proveedor
from .forms import ProveedorForm

# Vista para listar proveedores
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedor_list.html'
    context_object_name = 'proveedores'

# Vista para agregar un proveedor
class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor_form.html'

    def form_valid(self, form):
        form.instance.productos = self.request.POST.get('productos')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('proveedor_list')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedor_form.html'

    def form_valid(self, form):
        form.instance.productos = self.request.POST.get('productos')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('proveedor_list')

# Vista para eliminar un proveedor
class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')

# Vista para ver detalles de un proveedor
class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'proveedor_detail.html'
    context_object_name = 'proveedor'

# Vista para generar y guardar el CSV de proveedores en la carpeta Compartidos
class GenerarCSVView(View):
    def get(self, request, *args, **kwargs):
        # Crear la ruta de la carpeta Compartidos
        compartidos_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Compartidos')
        os.makedirs(compartidos_dir, exist_ok=True)  # Crea la carpeta si no existe

        # Generar el nombre del archivo CSV con la fecha actual
        filename = timezone.now().strftime("proveedores_%Y-%m-%d.csv")
        file_path = os.path.join(compartidos_dir, filename)

        # Crear y guardar el archivo CSV en la carpeta Compartidos
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nombre', 'Contacto', 'Email', 'Teléfono', 'Productos', 'Condiciones Comerciales'])

            # Escribir los datos de los proveedores
            proveedores = Proveedor.objects.all()
            for proveedor in proveedores:
                writer.writerow([
                    proveedor.id,
                    proveedor.nombre,
                    proveedor.contacto,
                    proveedor.email,
                    proveedor.telefono,
                    proveedor.productos,
                    proveedor.condiciones_comerciales
                ])

        # Devolver el archivo CSV como respuesta para su descarga directa
        response = HttpResponse(open(file_path, 'rb'), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
