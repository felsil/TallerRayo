# Generated by Django 3.2.5 on 2021-07-13 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaReparacion',
            fields=[
                ('nombreCategoria', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('numeroCategoria', models.IntegerField()),
            ],
        ),
    ]