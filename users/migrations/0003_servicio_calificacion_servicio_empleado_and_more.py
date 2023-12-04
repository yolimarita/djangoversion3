# Generated by Django 4.2.5 on 2023-12-03 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='calificacion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servicio',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='mensaje_calificacion',
            field=models.TextField(blank=True),
        ),
    ]
