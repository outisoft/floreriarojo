from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.ventas.views import cart, product, checkout

urlpatterns = [
    path('cart/',login_required(cart),name = 'cart'),
    path('product/',login_required(product),name = 'product'),
    path('checkout/',login_required(checkout),name = 'checkout'),
]
