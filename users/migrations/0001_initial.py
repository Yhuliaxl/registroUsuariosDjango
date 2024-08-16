# Generated by Django 5.1 on 2024-08-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('esatdo', models.CharField(choices=[('activo', 'activo'), ('inactivo', 'inactivo')], default='activo', max_length=100)),
                ('dateCreate', models.DateField(auto_now=True)),
            ],
        ),
    ]
