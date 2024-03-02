# Generated by Django 5.0.2 on 2024-02-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestion', '0014_alter_cliente_idcliente_alter_mascota_idmascota_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='mascotasAdopciones',
            fields=[
                ('idMascotaAdopcion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('edad', models.IntegerField(default=0)),
                ('castrado', models.BooleanField()),
                ('descripcion', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'MascotaAdopcion',
                'verbose_name_plural': 'MascotasAdopciones',
                'db_table': 'MascotasAdopciones',
            },
        ),
    ]
