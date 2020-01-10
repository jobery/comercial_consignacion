from django import forms

from .models import *

class TipoArticuloForm(forms.ModelForm):
    class Meta():
        model = TipoArticulo
        fields = ['nombre']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control',}),
        }

class ArticuloForm(forms.ModelForm):
    class Meta():
        model = Articulo
        fields = ['nombre',
            'TipoArticulo',
            'descripcion',
            'costo',
            'precio',
            'precio_cliente',]
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control',}),
            'TipoArticulo' : forms.Select(attrs={'class':'form-control',}),
            'descripcion' : forms.Textarea(attrs={'class':'form-control','rows':'3',}),
            'costo' : forms.NumberInput(attrs={'class':'form-control',}),
            'precio' : forms.NumberInput(attrs={'class':'form-control',}),
            'precio_cliente' : forms.NumberInput(attrs={'class':'form-control',}),
        }

class VendedorForm(forms.ModelForm):
    class Meta():
        model = Vendedor
        fields = [
            'nombre',
            'direccion',
            'dui',
            'telefono',
            'email',
        ]
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control',}),
            'direccion' : forms.Textarea(attrs={'class':'form-control','rows':'3',}),
            'dui' : forms.TextInput(attrs={'class':'form-control',}),
            'telefono' : forms.TextInput(attrs={'class':'form-control',}),
            'email' : forms.EmailInput(attrs={'class':'form-control',}),            
        }



# '__all__'
