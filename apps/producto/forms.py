from django import forms
from .models import Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','precio','cantidad','montoadicional', 'imagen')
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'cantidad': 'Cantidad Existente',
            'montoadicional': 'Monto Adicional',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre del producto',
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Precio del producto',
                }
            ),
            'cantidad': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese cantidad existentes',
                }
            ),
            'montoadicional': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el monto adicional',
                }
            )
        }
