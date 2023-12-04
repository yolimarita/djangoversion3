"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

from django.contrib import admin
from django.urls import path
from users import views  # Importa las vistas desde el mismo directorio (users)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('quienes_somos', views.quienes_somos, name="quienes_somos"),
    path('signup/', views.signup, name="registrarse"),
    path('logout/', views.cerrar_sesion, name="Cerrar sesión"),
    path('signin/', views.signin, name="Iniciar Sesion"),
    path('perfiles_empleadas', views.perfiles_empleadas, name="perfiles_empleadas"),
    path('contactenos', views.contactenos, name="contactenos"),
    path('servicios/', views.servicios, name='servicios'),
    path('solicitar_servicio/', views.solicitar_servicio, name="solicitar_servicio"),
    path('register/', views.registro_perfil, name='registro_perfil'),
    path('ver_perfil/<int:perfil_id>/', views.ver_perfil, name='ver_perfil'),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# myproject/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.urls import path
# from users import views
# from users.views import registro_perfil
# from django.urls import path
# #from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index,name="index"),
#     path('quienes_somos', views.quienes_somos,name="quienes_somos"),
#     path('signup/', views.signup,name="registrarse"),
#     path('logout/', views.cerrar_sesion,name="Cerrar sesión"),
#     path('signin/', views.signin,name="Iniciar Sesion"),
#     path('perfiles_empleadas', views.perfiles_empleadas,name="perfiles_empleadas"),
#     path('contactenos', views.contactenos,name="contactenos"),
#     path('servicios/', views.servicios, name='servicios'),
#     path('solicitar_servicio/', views.solicitar_servicio, name="solicitar_servicio"),
#     #path('register/', views.register_profile, name="registro_perfil"),
#      #path('', views.home, name='home'),
#     path('register/', views.registro_perfil, name='registro_perfil'),
#     #path('perfiles_empleadas/', views.listar_perfiles_empleadas, name='perfiles_empleadas'),
#     #path('perfiles_empleadas/<int:perfil_id>/', views.ver_perfil_empleada, name='ver_perfil_empleada'),
# ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    

    
    