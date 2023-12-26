# Generated by Django 4.2 on 2023-12-16 00:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_alter_empleados_rendimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='Correo',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='DNI',
            field=models.IntegerField(help_text='El DNI tener 8 digitos', validators=[django.core.validators.MaxValueValidator(99999999, message='Este campo debe tener exactamente 8 dígitos.'), django.core.validators.MinValueValidator(10000000, message='Este campo debe tener exactamente 8 dígitos.')]),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='Telefono',
            field=models.IntegerField(help_text='El numero de telefono debe tener 9 digitos', validators=[django.core.validators.MaxValueValidator(999999999, message='Este campo debe tener exactamente 9 dígitos.'), django.core.validators.MinValueValidator(900000000, message='Este campo debe tener exactamente 9 dígitos.')]),
        ),
    ]
