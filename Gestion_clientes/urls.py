from django.urls import path
from .views import home_nuevo_registro, home_principal, home_registros

urlpatterns = [
    path('', home_nuevo_registro, name='home_nuevo_registro'),
    path('home/', home_principal, name='home'),
    path('registros/', home_registros, name='home_registros')
]