# proveedor/management/commands/generate_csv.py
from django.core.management.base import BaseCommand
import csv
from proveedor.models import Proveedor
from django.utils import timezone

class Command(BaseCommand):
    help = 'Genera un archivo CSV de proveedores al final del día'

    def handle(self, *args, **kwargs):
        filename = timezone.now().strftime("proveedores_%Y-%m-%d.csv")
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nombre', 'Contacto', 'Email', 'Teléfono', 'Productos', 'Condiciones Comerciales'])

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
        self.stdout.write(self.style.SUCCESS(f'CSV generado exitosamente: {filename}'))
