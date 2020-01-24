from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy

from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

class CreateTipoArticulo(CreateView):
    model = TipoArticulo
    form_class = TipoArticuloForm
    template_name = 'tipoarticulo/creartipoarticulo.html'
    success_url = reverse_lazy('listartipoarticulo')

class ListTipoArticulo(ListView):
    model = TipoArticulo
    template_name = 'tipoarticulo/listartipoarticulo.html'

class UpdateTipoArticulo(UpdateView):
    model = TipoArticulo
    form_class = TipoArticuloForm
    template_name = 'tipoarticulo/editartipoarticulo.html'
    success_url = reverse_lazy('listartipoarticulo')

class DeleteTipoArticulo(DeleteView):
    model = TipoArticulo
    form_class = TipoArticuloForm
    template_name = 'tipoarticulo/eliminartipoarticulo.html'
    success_url = reverse_lazy('listartipoarticulo')

class ListArticulo(ListView):
    model = Articulo
    template_name = 'articulo/listararticulo.html'

class CreateArticulo(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/creararticulo.html'
    success_url = reverse_lazy('listararticulo')

class UpdateArticulo(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/editararticulo.html'
    success_url = reverse_lazy('listararticulo')

class DeleteArticulo(DeleteView):   
    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo/eliminararticulo.html'
    success_url = reverse_lazy('listararticulo')

class ListVendedor(ListView):
    model = Vendedor
    template_name = 'vendedor/listarvendedor.html'

class CreateVendedor(CreateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'vendedor/crearvendedor.html'
    success_url = reverse_lazy('listarvendedor')

class UpdateVendedor(UpdateView):
    model = Vendedor
    form_class = VendedorForm
    template_name = 'vendedor/editarvendedor.html'
    success_url = reverse_lazy('listarvendedor')

class DeleteVendedor(DeleteView):
    model =  Vendedor
    form_class = VendedorForm
    template_name = 'vendedor/eliminarvendedor.html'
    success_url = reverse_lazy('listarvendedor')

class ListGestor(ListView):
    model = Gestor
    template_name = 'gestor/listargestor.html'

class CreateGestor(CreateView):
    model = Gestor
    form_class = GestorForm
    template_name = 'gestor/creargestor.html'
    success_url = reverse_lazy('listargestor')

class UpdateGestor(UpdateView):
    model = Gestor
    form_class = GestorForm
    template_name = 'gestor/editargestor.html'
    success_url = reverse_lazy('listargestor')

class DeleteGestor(DeleteView):
    model = Gestor
    form_class = GestorForm
    template_name = 'gestor/eliminargestor.html'
    success_url = reverse_lazy('listargestor')

class ListConsigna(ListView):
    model = Consigna
    template_name = 'consigna/listarconsigna.html'

class CreateConsigna(CreateView):
    model = Consigna
    form_class = ConsignaForm
    template_name = 'consigna/crearconsigna.html'
    success_url = reverse_lazy('listarconsigna')

    def get(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_consigna_formset = DetalleConsignaFormSet()
        contexto = self.get_context_data(form=form,detalle_consigna_form_set=detalle_consigna_formset)
        return self.render_to_response(contexto)

    def post(self,request,*args,**kwargs):
        #self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        detalle_consigna_form_set = DetalleConsignaFormSet(request.POST)
        if form.is_valid() and detalle_consigna_form_set.is_valid():
            return self.form_valid(form,detalle_consigna_form_set)
        else:
            return self.form_invalid(form,detalle_consigna_form_set)

    def form_valid(self,form,detalle_consigna_form_set):        
        self.object = form.save()
        detalle_consigna_form_set.instance = self.object
        detalle_consigna_form_set.save()
        return HttpResponse(self.success_url)
        
    def form_invalid(self,form,detalle_consigna_form_set):
        context = self.get_context_data(form=form,detalle_consigna_form_set=detalle_consigna_form_set)
        return self.render_to_response(context)




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

