from django.db import models

# Create your models here.

class Producto(models.Model):
    Nombre_Producto = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=100)
    Precio_Venta = models.IntegerField(max_length=5)
    Precio_Compra = models.IntegerField(max_length=5)
    Clave_Producto = models.CharField(max_length=6)
    Existencias= models.IntegerField(max_length=5);
    COLORES=(('O','Oro'),('P','Plata'),('B','Bronce'),('R','Rosa'),('T','Turco'))
    color= models.CharField(max_length=1,choices=COLORES,default='O')

    def Nombre_Productos(self):
        cadena= "{0}, {1}"
        return cadena.format(self.Clave_Producto,self.Nombre_Producto)

    def __str__(self):
        return  self.Nombre_Productos()

class Vendedor(models.Model):
    Nombre_Pila_Vendedor = models.CharField(max_length=10)
    Apellido_Paterno_Vendedor= models.CharField(max_length=10)
    Apellido_Materno_Vendedor= models.CharField(max_length=10)
    Clave_Vendedor = models.AutoField(primary_key=True)

    def __str__(self):
        return "{0}, {1} {2}".format(self.Clave_Vendedor,self.Nombre_Pila_Vendedor,self.Apellido_Paterno_Vendedor)



class Venta(models.Model):
    Vendedor=models.ForeignKey(Vendedor, null=False,blank=False,on_delete=models.CASCADE)
    Producto=models.ForeignKey(Producto, null=False,blank=False,on_delete=models.CASCADE)
    num_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField(auto_now=True)
    cantidad = models.SmallIntegerField()

    def __str__(self):
        cadena = "{0} vendio {1} del producto {2} el {3}"
        return cadena.format(self.Vendedor,self.cantidad,self.Producto,self.fecha_venta)
