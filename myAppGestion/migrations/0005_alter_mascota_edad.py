# Generated by Django 5.0.2 on 2024-02-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestion', '0004_mascota_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='edad',
            field=models.IntegerField(default=0),
        ),
    ]
