from django.shortcuts import render

# Create your views here.

def home_nuevo_registro(request):
    return render(request, 'Registro/home_nuevo_registro.html')

def home_principal(request):
    return render(request, 'home.html')

def home_registros(request):
    return render(request, 'Registro/home_registros.html')