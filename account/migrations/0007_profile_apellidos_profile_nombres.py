# Generated by Django 4.1.4 on 2023-10-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_delete_usermodification'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apellidos',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nombres',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
