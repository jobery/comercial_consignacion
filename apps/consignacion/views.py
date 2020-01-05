from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView

from .models import TipoArticulo
from .forms import TipoArticuloForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def CrearTipoArticulo(request):
    if request.method == 'POST':
        form = TipoArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TipoArticuloForm()
    return render(request,'consignacion/creartipoarticulo.html',{'form':form})
        

