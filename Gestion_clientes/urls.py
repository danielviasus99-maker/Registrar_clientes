from django.urls import path
from .views import home_nuevo_registro, home_principal

urlpatterns = [
    path('', home_nuevo_registro, name='home_nuevo_registro'),
    path('', home_principal, name='home'),
]