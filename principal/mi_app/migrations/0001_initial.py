# Generated by Django 5.0.1 on 2024-07-18 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateField()),
                ('genero', models.CharField(choices=[('Terror', 'Terror'), ('Accion', 'Accion'), ('Ciencia Ficcion', 'Ciencia Ficcion'), ('Romance', 'Romance'), ('Comedia', 'Comedia')], max_length=40)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro', to='mi_app.autor')),
            ],
        ),
    ]
