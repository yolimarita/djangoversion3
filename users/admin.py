from django.contrib import admin
from .models import Servicio
#from .models import UserProfile 
from .models import PerfilEmpleado


admin.site.register(Servicio)
admin.site.register(PerfilEmpleado)
#admin.site.register(UserProfile)

