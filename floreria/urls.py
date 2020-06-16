from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.urls import path,include
from apps.inicio.views import Inicio
from apps.usuario.views import Login,logoutUsuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/',include(('apps.producto.urls','producto'))),
    path('usuarios/',include(('apps.usuario.urls','usuarios'))),
    path('ventas/',include(('apps.ventas.urls','ventas'))),
    path('',Inicio.as_view(), name = 'index'),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('logout/', login_required(logoutUsuario), name = 'logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
