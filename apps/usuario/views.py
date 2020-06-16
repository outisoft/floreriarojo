import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from apps.usuario.models import Usuario
from .forms import FormularioLogin, FormularioUsuario, UserForm

class Login(FormView):
    template_name = 'inicio/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/')

class Registrar(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'inicio/register.html'
    success_url = reverse_lazy('usuarios:user')

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'inicio/register.html'
    def post(self, request, *args, **kwargs):

            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_usuario = Usuario(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('username'),
                    nombres=form.cleaned_data.get('nombres'),
                    apellidos=form.cleaned_data.get('apellidos')
                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()
                #mensaje = f'{self.model.__name__} registrado correctamente!'
                #error = 'No hay error!'
                #response = JsonResponse({'mensaje':mensaje,'error':error})
                #response.status_code = 201
                return redirect('usuarios:user')
            else:
                mensaje = f'{self.model.__name__} no se ha podido registrar!'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
                """
        if request.is_ajax():
        else:
            return redirect('/')
            """
def user(request):
    return render(request, "user.html")


class ActualizarPerfil(UpdateView):
    model = Usuario
    form_class = UserForm
    template_name = 'usuarios/edit_perfil.html'
    success_url = reverse_lazy('usuarios:user')
