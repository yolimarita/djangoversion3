from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Servicio, PerfilEmpleado
from .forms import SolicitarServicioForm, RegistroPerfilEmpleadoForm
from .models import PerfilEmpleado
from django.http import HttpResponse
from django.core.mail import send_mail
from django import forms


class AceptarForm(forms.Form):
    aceptar = forms.BooleanField(label='¿Aceptar este perfil?')

def ver_perfil(request, perfil_id):
    perfil = get_object_or_404(PerfilEmpleado, id=perfil_id)

    if request.method == 'POST':
        form = AceptarForm(request.POST)
        if form.is_valid():
            aceptar_perfil = form.cleaned_data['aceptar']

            if aceptar_perfil:
                perfil.servicio_aceptado = True
                perfil.save()

                # Lógica para enviar la orden de pago al correo del cliente
                enviar_orden_al_correo(perfil, request.user.email)

                return HttpResponse("Orden de pago generada y enviada al correo del cliente.")
                
    else:
        form = AceptarForm()

    return render(request, 'ver_perfil.html', {'perfil': perfil, 'form': form})

def enviar_orden_al_correo(perfil, correo_cliente):
    # Lógica para construir y enviar el correo con la orden de pago
    # ...

    send_mail(
        'Asunto del Correo',
        'Cuerpo del Correo con la orden de pago para el perfil {}'.format(perfil.nombre_completo),
        'tu_correo@gmail.com',  # Remitente del correo
        [correo_cliente],  # Destinatario del correo
        fail_silently=False,
    )

import logging

logger = logging.getLogger(__name__)

@login_required
def solicitar_servicio(request):
    if request.method == 'POST':
        form = SolicitarServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.cliente = request.user
            servicio.save()
            return redirect('perfiles_empleadas')  # Ajusta la redirección según tus necesidades
    else:
        form = SolicitarServicioForm()
    return render(request, 'solicitar_servicio.html', {'form': form})

@login_required
def registro_perfil(request):
    if request.method == 'POST':
        form = RegistroPerfilEmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            perfil_empleado = form.save(commit=False)
            perfil_empleado.user = request.user
            perfil_empleado.save()
            return redirect('perfiles_empleadas')  # Ajusta la redirección según tus necesidades
    else:
        form = RegistroPerfilEmpleadoForm()
    return render(request, 'registro_perfil.html', {'form': form})

def perfiles_empleadas(request):
    perfiles = PerfilEmpleado.objects.all()

    # Imprimir perfiles en la consola
    for perfil in perfiles:
        print(f"Perfil: {perfil.nombre_completo}")

    # Pasa los perfiles al contexto de la plantilla
    print(perfiles)  # Agrega esta línea para imprimir perfiles
    return render(request, 'perfiles_empleadas.html', {'perfiles': perfiles})


def concretar_servicio(request, perfil_id):
    perfil = get_object_or_404(PerfilEmpleado, id=perfil_id)
    # Lógica para generar una orden de pago
    # ...

    return render(request, 'orden_pago.html', {'perfil': perfil, 'orden_generada': True})



def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email']
                )
                user.save()  # Guardar el usuario en la base de datos
                login(request, user)
                return redirect('servicios')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Usuario ya existe',
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            'error': 'Contraseña no coincide',
        })

def servicios(request):
    return render(request, 'servicios.html')


def cerrar_sesion(request):
    logout(request)
    # Puedes redirigir a la página que desees después de cerrar sesión
    return redirect('index')


def signin(request): 
        if request.method == 'GET': 
            return render(request, 'signin.html', { 
                'form': AuthenticationForm() 
            }) 
        else: 
            user = authenticate( 
                request, username=request.POST['username'], password=request.POST['password']) 
            if user is None: 
                return render(request, 'signin.html', { 
                    'form': AuthenticationForm(), 
                    'error': 'Usuario o contraseña incorrectos' 
                }) 
            else: 
                login(request, user) 
                return redirect('servicios')

def index(request):
    return render(request, "index.html")

def quienes_somos(request):
    return render(request, "quienes_somos.html")

def registrarse(request):
    return render(request, "registrarse.html")


def contratar_servicio(request):
    return render(request, "contratar_servicio.html")

def contactenos(request):
    return render(request, "contactenos.html")





