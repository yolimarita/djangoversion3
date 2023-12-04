
from django import forms
from .models import PerfilEmpleado, Servicio 

class SolicitarServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['tipo_servicio', 'tipo_pago', 'direccion_servicio']

class RegistroPerfilEmpleadoForm(forms.ModelForm):
    class Meta:
        model = PerfilEmpleado
        fields = ['nombre_completo', 'numero_celular', 'zona_trabajo', 'email', 'foto_perfil', 'habilidades']


class AceptarForm(forms.Form):
    aceptar = forms.BooleanField(label='¿Aceptar este perfil?')
