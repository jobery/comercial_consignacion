from django.urls import path

#from apps.consignacion.views import index,CrearTipoArticulo,ListarTipoArticulo,EditarTipoArticulo,EliminarTipoArticulo
from apps.consignacion.views import *

urlpatterns = [
    path('',index,name='index'),
    path('creartipoarticulo/',CreateTipoArticulo.as_view(),name='creartipoarticulo'),
    path('listartipoarticulo/',ListTipoArticulo.as_view(),name='listartipoarticulo'),
    path('editartipoarticulo/<int:pk>',UpdateTipoArticulo.as_view(),name='editartipoarticulo'),
    path('eliminartipoarticulo/<int:pk>',DeleteTipoArticulo.as_view(),name='eliminartipoarticulo'),
    path('listararticulo/',ListArticulo.as_view(),name='listararticulo'),
    path('creararticulo/',CreateArticulo.as_view(),name='creararticulo'),
    path('editararticulo/<int:pk>',UpdateArticulo.as_view(),name='editararticulo'),
    path('eliminararticulo/<int:pk>',DeleteArticulo.as_view(),name='eliminararticulo'),
    path('listarvendedor/',ListVendedor.as_view(),name='listarvendedor'),
    path('crearvendedor/',CreateVendedor.as_view(),name='crearvendedor'),
    path('editarvendedor/<int:pk>',UpdateVendedor.as_view(),name='editarvendedor'),
    path('eliminarvendedor/<int:pk>',DeleteVendedor.as_view(),name='eliminarvendedor'), 
    path('listargestor/',ListGestor.as_view(),name='listargestor'),
    path('creargestor/',CreateGestor.as_view(),name='creargestor'),
    path('editargestor/<int:pk>',UpdateGestor.as_view(),name='editargestor'),
    path('eliminargestor/<int:pk>',DeleteGestor.as_view(),name='eliminargestor'),     
    path('listarconsigna/',ListConsigna.as_view(),name='listarconsigna'),
    path('crearconsigna/',CreateConsigna.as_view(),name='crearconsigna'),
]
