from django.db import models

# Create your models here.

class TipoArticulo(models.Model):
    nombre = models.CharField("Tipo de Articulo",max_length = 45,blank = False,null = False)

    class Meta():
        verbose_name = 'Tipo de Articulo'
        verbose_name_plural = 'Tipos de Articulos'
        ordering = ['id']

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField("Nombre",max_length = 150,blank = False,null = False)
    TipoArticulo = models.ForeignKey(TipoArticulo,on_delete = models.DO_NOTHING,null = True,blank = True)
    descripcion = models.TextField("Descripcion")
    costo = models.DecimalField("Costo",max_digits = 12,decimal_places = 2,blank = False,null = True)
    precio = models.DecimalField("Precio",max_digits = 12,decimal_places = 2,blank = False,null = True)
    precio_cliente = models.DecimalField("Precio Cliente",max_digits = 12,decimal_places = 2,blank = False,null = True)
    existencia = models.IntegerField("Existencia")

    class Meta():
        verbose_name = 'Articulo'    
        verbose_name_plural = 'Articulos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField("Nombre",max_length = 150,blank = False,null = False)
    direccion = models.TextField("Direccion")
    dui = models.CharField("D.U.I.",max_length = 15,blank = False,null = False)
    telefono = models.CharField("Telefono",max_length = 15,blank = False,null = False)
    email = models.EmailField("Correo",blank = True,null = True)    

    class Meta():
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Gestor(models.Model):
    nombre = models.CharField("Nombre",max_length = 150,blank = False,null = False)
    dui = models.CharField("D.U.I.",max_length = 15,blank = False,null = False)
    telefono = models.CharField("Telefono",max_length = 15,blank = False,null = False) 
    email = models.EmailField("Correo",blank = True,null = True)  

    class Meta():
        verbose_name = 'Gestor'
        verbose_name_plural = 'Gestores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Consigna(models.Model):
    vendedor = models.ForeignKey(Vendedor,on_delete = models.DO_NOTHING,blank = False,null = False)
    gestor = models.ForeignKey(Gestor,on_delete = models.DO_NOTHING,blank = False,null = False)
    fecha = models.DateField("Fecha",blank = False,null = False)
    fecha_recibe = models.DateField("Fecha Recibe",blank = True,null = True)
    fecha_entrega = models.DateField("Fecha Entrega",blank = True,null = True)    
    viatico = models.DecimalField("Viatico",max_digits = 12,decimal_places = 2,blank = False,null = True)
    panalizacion = models.DecimalField("Penalizacion",max_digits = 12,decimal_places = 2,blank = False,null = True) 
    observacion = models.TextField("Observaciones",blank = True,null = True)
    completa = models.BooleanField("Consigna Completa")

    class Meta():
        verbose_name = 'Consigna'
        verbose_name_plural = 'Consignas'
        ordering = ['id','fecha']

    def __str__(self):
        return 'Fecha %s Vendedor %s' % (self.fecha,self.vendedor)

class DetalleConsigna(models.Model):
    consigna = models.ForeignKey(Consigna,on_delete = models.CASCADE,related_name = 'items',blank = False,null = False)
    articulo = models.ForeignKey(Articulo,on_delete = models.CASCADE,blank = False,null = False)
    cantidad = models.IntegerField("Cantidad",blank = False,null = False)
    precio = models.DecimalField("Precio",max_digits = 12,decimal_places = 2,blank = False,null = True)
    total = models.DecimalField("Total",max_digits = 12,decimal_places = 2,blank = False,null = True)

    class Meta():
        verbose_name = 'Detalle de Consigna'
        verbose_name_plural = 'Detalle de Consignas'
        ordering = ['id']

    def __str__(self):
        return 'Cantidad %s Producto %s' % (self.cantidad,self.articulo)













