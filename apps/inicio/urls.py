from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,ListadoProductos

urlpatterns = [
    path('', LoginView.as_view(template_name="index.html"), name="index"),
    path('listado_productos/', ListadoProductos.as_view(), name = 'listado_productos'),
]
