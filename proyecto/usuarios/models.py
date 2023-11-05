from django.db import models
from django.contrib.auth.models import AbstractUser

# El modelo User hereda de AbstractUser todas 
# la caracteristicas de un user de Django 
 
# Se agregan los atributos apodo y pronombre
class User(AbstractUser):
  pronombres = [('La','La'),('El','El'), ('Le','Le'),('Otro','Otro')]
  pronombre = models.CharField(max_length=5,choices=pronombres)
  apodo = models.CharField(max_length=30)