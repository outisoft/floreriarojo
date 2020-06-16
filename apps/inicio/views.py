from django.shortcuts import render
from apps.producto.models import Producto
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from apps.producto.forms import FormularioProducto
from django.urls import reverse_lazy

# Create your views here.

class Inicio(View):
    model = Producto
    form_class = FormularioProducto
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())


class ListadoProductos(TemplateView):
    """Clase que renderiza el index del sistema"""

    template_name = 'index.html'
