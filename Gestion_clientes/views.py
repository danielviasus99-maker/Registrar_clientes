from django.shortcuts import render, redirect
from .models import Cliente, OrdenServicio, FotoOrden

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

        return redirect('home_registros')

    return render(request, 'Registro/home_nuevo_registro.html')

def home_principal(request):
    return render(request, 'home.html')

def home_registros(request):
    return render(request, 'Registro/home_registros.html')