# Generated by Django 5.0.2 on 2024-02-07 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestion', '0002_cliente_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='descripcion',
            field=models.TextField(default='Ingresa descripcion mascota', max_length=500),
        ),
    ]