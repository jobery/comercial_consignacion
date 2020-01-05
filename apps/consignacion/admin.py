from django.contrib import admin

from .models import Articulo,TipoArticulo,Vendedor,Gestor,Consigna,DetalleConsigna

# Register your models here.

admin.site.register(Articulo)
admin.site.register(TipoArticulo)
admin.site.register(Vendedor)
admin.site.register(Gestor)

class DetalleConsignaInline(admin.TabularInline):
    model = DetalleConsigna

class ConsignaAdmin(admin.ModelAdmin):
    inlines = (DetalleConsignaInline,)

#admin.site.register(ConsignaAdmin,inlines = (ConsignaAdmin,))
#admin.site.register(DetalleConsigna)
#admin.site.register(DetalleConsignaInline,ConsignaAdmin)

admin.site.register(Consigna)
admin.site.register(DetalleConsigna)