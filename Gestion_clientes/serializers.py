from rest_framework import serializers
from .models import Cliente, OrdenServicio, FotoOrden


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'telefono', 'email']


class FotoOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoOrden
        fields = ['id', 'orden', 'imagen', 'fecha_subida']
        read_only_fields = ['fecha_subida']


class OrdenServicioSerializer(serializers.ModelSerializer):
    # Para lectura: muestra el cliente completo
    cliente_detalle = ClienteSerializer(source='cliente', read_only=True)
    # Para escritura: solo se envía el id del cliente
    fotos = FotoOrdenSerializer(many=True, read_only=True)

    class Meta:
        model = OrdenServicio
        fields = [
            'id', 'cliente', 'cliente_detalle', 'dispositivo',
            'descripcion_dano', 'valor_reparacion', 'abono_inicial',
            'estado', 'fecha_creacion', 'fecha_actualizacion', 'fotos',
        ]
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']