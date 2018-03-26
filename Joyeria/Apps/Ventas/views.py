from django.shortcuts import render
from .models import Producto
# Create your views here.
def inicio(request):
    articulos = Producto.objects.all().order_by('Clave_Producto')
    return render(request,"index.html",{'articulos':articulos})


def registro(request):
    return render(request,"Registro.html",{})

