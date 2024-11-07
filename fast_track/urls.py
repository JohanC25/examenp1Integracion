# fast_track/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import inicio  # Importa la vista de inicio desde views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proveedor/', include('proveedor.urls')),
    path('facturacion/', include('facturacion.urls')),
    path('', inicio, name='inicio'),  # Define la ruta de inicio aquí
]