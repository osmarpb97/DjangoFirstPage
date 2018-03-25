from django.contrib import admin
from Joyeria.Apps.Ventas.models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Comprador)
admin.site.register(Venta)