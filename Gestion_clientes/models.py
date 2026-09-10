from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField("Nombre completo", max_length=150)
    telefono = models.CharField("Teléfono de contacto", max_length=15)
    email = models.EmailField("Email de notificación", blank=True, null=True)

    def __str__(self):
        return self.nombre


class OrdenServicio(models.Model):
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("en_proceso", "En Proceso"),
        ("completado", "Completado"),
        ("entregado", "Entregado"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ordenes")
    dispositivo = models.CharField("Marca y modelo del dispositivo", max_length=150)
    descripcion_dano = models.TextField("Descripción del daño / síntomas")
    valor_reparacion = models.PositiveIntegerField("Valor de la reparación (COP)", default=0)
    abono_inicial = models.PositiveIntegerField("Abono inicial (COP)", default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="pendiente")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Orden #{self.id} - {self.cliente.nombre}"


def ruta_foto_orden(instance, filename):
    return f"ordenes/{instance.orden.id}/{filename}"


class FotoOrden(models.Model):
    orden = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE, related_name="fotos")
    imagen = models.ImageField("Foto", upload_to=ruta_foto_orden)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto de Orden #{self.orden.id}"