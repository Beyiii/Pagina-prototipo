from django.db import models
from django.utils import timezone
from categorias.models import Categoria
from usuarios.models import User

# El modelo Ficha hereda de model.Model todas
# las caracteristicas de un model de Django.

# Ficha será el modelo de los movimientos de dinero del usuario.

class Ficha(models.Model): 
    # Nombre que le dará el usuario a su movimiento
    titulo = models.CharField(max_length=250)  # un varchar

    # Dinero el que será sumado o restado al monto final
    monto = models.CharField(max_length=250) # un varchar

    # Fecha en el que creo el nuevo movimiento
    fecha_creacion = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))  # un date

    # Si el movimiento es un egreso o ingreso
    tipo = models.ForeignKey(Categoria, default="general", on_delete=models.CASCADE)  # la llave foránea
    
    # El usuario al que pertenece esta ficha
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)


