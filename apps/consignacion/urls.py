from django.urls import path

from apps.consignacion.views import index,CrearTipoArticulo

urlpatterns = [
    path('',index,name='index'),
    path('creartipoarticulo/',CrearTipoArticulo,name='creartipoarticulo'),
]
