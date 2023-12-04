# En users/models.py

from django.db import models
from django.contrib.auth.models import User

class PerfilEmpleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=255)
    numero_celular = models.CharField(max_length=15)
    zona_trabajo = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    foto_perfil = models.ImageField(upload_to='perfil_empleado/', null=True, blank=True)
    habilidades = models.TextField(max_length=255)

class Servicio(models.Model):
    TIPOS_SERVICIO = [
        ('limpiar_casa', 'Limpiar mi casa'),
        ('limpiar_empresa', 'Limpiar mi empresa'),
        ('cuidado_ninos', 'Cuidado de niños'),
        ('cuidado_adulto_mayor', 'Cuidado del adulto mayor'),
        ('empleadas_dias', 'Empleadas por días'),
        ('empleadas_horas', 'Empleadas por horas'),
        ('empleadas_internas', 'Empleadas internas'),
    ]

    TIPOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('corresponsal_bancario', 'Corresponsal Bancario'),
        ('debito', 'Tarjeta de Débito'),
        ('credito', 'Tarjeta de Crédito'),
    ]
    CALIFICACION_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_servicio = models.CharField(max_length=50, choices=TIPOS_SERVICIO)
    tipo_pago = models.CharField(max_length=50, choices=TIPOS_PAGO)
    direccion_servicio = models.TextField(max_length=150, null=True, blank=True)
    empleado_seleccionado = models.ForeignKey(PerfilEmpleado, on_delete=models.CASCADE, null=True, blank=True)
    calificacion_cliente = models.IntegerField(choices=CALIFICACION_CHOICES, null=True, blank=True)
