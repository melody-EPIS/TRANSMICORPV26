# Generated by Django 4.1.4 on 2023-10-13 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0004_profile_puestotrabajo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('puestoTrabajo', models.CharField(blank=True, max_length=80, null=True)),
                ('new_password', models.CharField(blank=True, max_length=128, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='modification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
