# Generated by Django 4.2.7 on 2023-11-30 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField()),
                ('fecha_agenda', models.DateField()),
                ('tipo_servicio', models.CharField(choices=[('EH', 'Empleadas por horas'), ('ED', 'Empleadas por días'), ('EI', 'Empleadas internas'), ('LE', 'Limpiar mi Empresa'), ('LC', 'Limpiar mi casa'), ('CN', 'Cuidado de niños'), ('CA', 'Cuidado del adulto mayor')], max_length=2)),
                ('metodo_pago', models.CharField(choices=[('EF', 'Efectivo'), ('TC', 'Tarjeta de crédito'), ('PP', 'PayPal')], max_length=2)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]