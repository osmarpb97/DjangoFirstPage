from django.contrib import admin
from Joyeria.Apps.Ventas.models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Vendedor)
admin.site.register(Venta)