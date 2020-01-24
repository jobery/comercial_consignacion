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

class GestorForm(forms.ModelForm):
    class Meta():
        model = Gestor
        fields = [
            'nombre',
            'dui',
            'telefono',
            'email',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control',}),
            'dui': forms.TextInput(attrs={'class':'form-control',}),
            'telefono': forms.TextInput(attrs={'class':'form-control',}),
            'email': forms.EmailInput(attrs={'class':'form-control',}),
        }

class ConsignaForm(forms.ModelForm):
    class Meta():
        model = Consigna
        fields = [
            'vendedor',
            'gestor',
            'fecha',
            'fecha_recibe',
            'fecha_entrega',
            'viatico',
            'penalizacion',
            'observacion',
            'completa',
        ]
        widgets = {
            'vendedor': forms.Select(attrs={'class':'form-control',}),
            'gestor': forms.Select(attrs={'class':'form-control',}),
            'fecha': forms.DateInput(attrs={'class':'form-control','type':'date',},format='%Y-%m-%d'),
            'fecha_recibe':forms.DateInput(attrs={'class':'form-control','type':'date',},format='%Y-%m-%d'),
            'fecha_entrega': forms.DateInput(attrs={'class':'form-control','type':'date',},format='%Y-%m-%d'),
            'viatico': forms.NumberInput(attrs={'class':'form-control',}),
            'penalizacion': forms.NumberInput(attrs={'class':'form-control',}),
            'observacion': forms.Textarea(attrs={'class':'form-control',}),
            'completa': forms.CheckboxInput(attrs={'type':'checkbox',}),
        }

class DetalleConsignaForm(forms.ModelForm):
    class Meta():
        model = DetalleConsigna
        fields = [
            'articulo',
            'cantidad',
            'precio',
            'total',
        ]
        widgets = {
            'articulo': forms.Select(attrs={'class':'form-control',}),
            'cantidad': forms.NumberInput(attrs={'class':'form-control',}),
            'precio': forms.NumberInput(attrs={'class':'form-control',}),
            'total': forms.NumberInput(attrs={'class':'form-control',}),
        }
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == '':
            raise forms.ValidationError('Especificar Cantidad')
        return cantidad

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio == '':
            raise forms.ValidationError('Especifique Precio')
        return precio
    
    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data['total'] = cleaned_data['cantidad'] * cleaned_data['precio']
        return cleaned_data

DetalleConsignaFormSet = forms.models.inlineformset_factory(Consigna, DetalleConsigna,form=DetalleConsignaForm,extra=5)

# '__all__'
