from django.urls import path, include
from .views import home_nuevo_registro, home_principal, home_registros
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, OrdenServicioViewSet, FotoOrdenViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'ordenes', OrdenServicioViewSet)
router.register(r'fotos', FotoOrdenViewSet)

urlpatterns = [
    path('', home_nuevo_registro, name='home_nuevo_registro'),
    path('home/', home_principal, name='home'),
    path('api/', include(router.urls)),
    path('registros/', home_registros, name='home_registros')
]