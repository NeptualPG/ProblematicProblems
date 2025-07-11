# Generated by Django 5.2.2 on 2025-06-12 01:43

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(error_messages={'unique': 'Ya existe un usuario con este email.'}, max_length=255, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='Correo electrónico')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de registro')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Equipo')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
