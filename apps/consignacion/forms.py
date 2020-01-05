from django import forms

from .models import TipoArticulo

class TipoArticuloForm(forms.ModelForm):
    class Meta():
        model = TipoArticulo
        fields = ['nombre']