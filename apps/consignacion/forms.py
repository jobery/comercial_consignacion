from django import forms

from .models import *

class TipoArticuloForm(forms.ModelForm):
    class Meta():
        model = TipoArticulo
        fields = ['nombre']

class ArticuloForm(forms.ModelForm):
    class Meta():
        model = Articulo
        fields = ['nombre',
            'TipoArticulo',
            'descripcion',
            'costo',
            'precio',
            'precio_cliente',]

# '__all__'
# {{ form.as_p }}