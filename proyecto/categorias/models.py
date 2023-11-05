from django.db import models

# El modelo Categoria hereda de model.Model todas
# las caracteristicas de un model de Django.

# Servirá para identificar el tipo de ficha (movimiento) que es.

class Categoria(models.Model):
    # Este atributo será el tipo de movimiento que se creará (Ingreso o Egreso)
    nombre = models.CharField(max_length=100) 

    def __str__(self):
        return self.nombre  # permite definir cómo se mostrará una categoría al imprmirla.

