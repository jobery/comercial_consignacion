from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy

from .models import TipoArticulo
from .forms import TipoArticuloForm

# Create your views here.
def index(request):
    return render(request,'index.html')

class CreateTipoArticulo(CreateView):
    model = TipoArticulo
    form_class = TipoArticuloForm
    template_name = 'consignacion/creartipoarticulo.html'
    success_url = reverse_lazy('listartipoarticulo')

class ListTipoArticulo(ListView):
    model = TipoArticulo
    template_name = 'consignacion/listartipoarticulo.html'

class UpdateTipoArticulo(UpdateView):
    model = TipoArticulo
    form_class = TipoArticuloForm
    template_name = 'consignacion/editartipoarticulo.html'
    success_url = reverse_lazy('listartipoarticulo')

class DeleteTipoArticulo(DeleteView):
    model = TipoArticulo
    form_class = TipoArticuloForm
    template_name = 'consignacion/eliminartipoarticulo.html'
    success_url = reverse_lazy('listartipoarticulo')


def CrearTipoArticulo(request):
    if request.method == 'POST':
        form = TipoArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listartipoarticulo')
    else:
        form = TipoArticuloForm()
    return render(request,'consignacion/creartipoarticulo.html',{'form':form})

def ListarTipoArticulo(request):
    tipoarticulos = TipoArticulo.objects.all()
    context = {'tipoarticulos':tipoarticulos}
    return render(request,'consignacion/listartipoarticulo.html',context)

def EditarTipoArticulo(request,id):
    tipoarticulo = TipoArticulo.objects.get(id = id)
    if request.method == 'GET':
        form = TipoArticuloForm(instance = tipoarticulo)
    else:
        form = TipoArticuloForm(request.POST,instance = tipoarticulo)
        if form.is_valid():
            form.save()
        return redirect('listartipoarticulo')
    return render(request,'consignacion/creartipoarticulo.html',{'form':form})

def EliminarTipoArticulo(request,id):
    tipoarticulo = TipoArticulo.objects.get(id = id)
    if request.method == 'POST':
        tipoarticulo.delete()
        return redirect('listartipoarticulo')
    return render(request,'consignacion/eliminartipoarticulo.html',{'tipoarticulo':tipoarticulo})

