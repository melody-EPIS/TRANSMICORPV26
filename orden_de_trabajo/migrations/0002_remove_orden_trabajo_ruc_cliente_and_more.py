# Generated by Django 4.2.3 on 2023-11-29 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unidades', '0004_alter_unidades_capacidad_carga'),
        ('empleados', '0004_alter_empleados_rendimiento'),
        ('orden_de_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden_trabajo',
            name='RUC_cliente',
        ),
        migrations.AlterField(
            model_name='orden_trabajo',
            name='Id_Conductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleados'),
        ),
        migrations.AlterField(
            model_name='orden_trabajo',
            name='Id_Vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidades.unidades'),
        ),
    ]
