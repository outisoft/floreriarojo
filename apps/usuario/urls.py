from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.usuario.views import RegistrarUsuario, Registrar, user,ActualizarPerfil

urlpatterns = [
    #path('listado_usuarios/', login_required(ListadoUsuario.as_view()),{'parametro_extra': 'Hola!'},name='listar_usuarios'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name = 'registrar_usuario'),
    path('user/',login_required(user),name = 'user'),
    path('edit_perfil/<int:pk>/',login_required(ActualizarPerfil.as_view()),name = 'edit_perfil'),
]

#URLS DE VISTAS IMPLICITAS
urlpatterns += [
    path('inicio_usuarios/', login_required(TemplateView.as_view(template_name='/')), name='inicio_usuarios'),
]
