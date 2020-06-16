from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.producto.views import AgregarProducto, ListadoProductos,ActualizarProducto

urlpatterns = [
    path('agregar_producto/',login_required(AgregarProducto.as_view()),name = 'agregar_producto'),

    path('listado_productos/', ListadoProductos.as_view(), name = 'listado_productos'),

    path('editar_producto/<int:pk>/', login_required(ActualizarProducto.as_view()), name = 'editar_producto'),
]
