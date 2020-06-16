from django.shortcuts import render
from apps.producto.models import Producto
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from .forms import FormularioProducto
from django.urls import reverse_lazy

class AgregarProducto(CreateView):
    model = Producto
    form_class = FormularioProducto
    template_name = 'agregar_producto.html'
    success_url = reverse_lazy('producto:agregar_producto')

class ListadoProductos(View):
    model = Producto
    form_class = FormularioProducto
    template_name = 'producto/listar_productos.html'

    def get_queryset(self):
        return self.model.objects.filter(estado = True)

    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['productos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())

class ActualizarProducto(UpdateView):
    model = Producto
    form_class = FormularioProducto
    template_name = 'producto/editar_producto.html'
    success_url = reverse_lazy('producto:listado_productos')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.filter(estado = True)
        return context
