# facturacion/urls.py
from django.urls import path
from .views import (
    FacturaListView, FacturaCreateView, FacturaUpdateView, FacturaDeleteView, FacturaDetailView, VistaPreviaCSVView, CargarCSVView
)

urlpatterns = [
    path('', FacturaListView.as_view(), name='facturacion_list'),  # Esta línea debe estar presente
    path('nuevo/', FacturaCreateView.as_view(), name='factura_create'),
    path('<int:pk>/editar/', FacturaUpdateView.as_view(), name='factura_update'),
    path('<int:pk>/eliminar/', FacturaDeleteView.as_view(), name='factura_delete'),
    path('<int:pk>/', FacturaDetailView.as_view(), name='factura_detail'),
    path('vista-previa-csv/', VistaPreviaCSVView.as_view(), name='vista_previa_csv'),
    path('cargar-csv/', CargarCSVView.as_view(), name='cargar_csv'),
]
