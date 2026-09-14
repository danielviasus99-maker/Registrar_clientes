from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cliente, OrdenServicio, FotoOrden
from rest_framework import viewsets
from .serializers import ClienteSerializer, OrdenServicioSerializer, FotoOrdenSerializer

# Create your views here.

def home_nuevo_registro(request):
    if request.method == "POST":
        cliente = Cliente.objects.create(
            nombre=request.POST.get("nombre"),
            telefono=request.POST.get("telefono"),
            email=request.POST.get("email") or None,
        )

        orden = OrdenServicio.objects.create(
            cliente=cliente,
            dispositivo=request.POST.get("dispositivo"),
            descripcion_dano=request.POST.get("descripcion_dano"),
            valor_reparacion=request.POST.get("valor_reparacion") or 0,
            abono_inicial=request.POST.get("abono_inicial") or 0,
        )

        fotos = request.FILES.getlist("fotos")
        for foto in fotos[:5]:
            FotoOrden.objects.create(orden=orden, imagen=foto)

        return redirect(f"{reverse('home_nuevo_registro')}?exito=1")

    exito = request.GET.get('exito') == '1'
    return render(request, 'Registro/home_nuevo_registro.html', {'exito': exito})


def home_principal(request):
    return render(request, 'home.html')


def home_registros(request):
    ordenes = OrdenServicio.objects.select_related('cliente').prefetch_related('fotos').order_by('-fecha_creacion')
    return render(request, 'Registro/home_registros.html', {'ordenes': ordenes})

#Clases de API REST Framework
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('-id')
    serializer_class = ClienteSerializer


class OrdenServicioViewSet(viewsets.ModelViewSet):
    queryset = OrdenServicio.objects.all().order_by('-fecha_creacion')
    serializer_class = OrdenServicioSerializer


class FotoOrdenViewSet(viewsets.ModelViewSet):
    queryset = FotoOrden.objects.all()
    serializer_class = FotoOrdenSerializer




















