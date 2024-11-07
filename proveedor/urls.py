from django.urls import path
from .views import ProveedorListView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView, ProveedorDetailView, GenerarCSVView

urlpatterns = [
    path('', ProveedorListView.as_view(), name='proveedor_list'),
    path('nuevo/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedor_delete'),
    path('<int:pk>/', ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('generar_csv/', GenerarCSVView.as_view(), name='generar_csv'),  # URL para generar CSV
]
