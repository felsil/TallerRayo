# Generated by Django 3.2.5 on 2021-07-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miTaller', '0003_reparacion_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('nombreContacto', models.CharField(max_length=50)),
                ('apellidoContacto', models.CharField(max_length=50)),
                ('emailContacto', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fonoContacto', models.IntegerField()),
                ('mensajeContacto', models.TextField()),
            ],
        ),
    ]
