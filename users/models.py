from django.db import models

# Create your models here.
class persona (models.Model):
    estado_choise =[
        ("activo", "activo"),
        ("inactivo","inactivo"),
    ]
    name= models.CharField(max_length=100)
    cedula= models.CharField(max_length=100)
    telefono= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    esatdo= models.CharField(max_length=100, choices=estado_choise, default="activo")
    dateCreate= models.DateField(auto_now=True)

