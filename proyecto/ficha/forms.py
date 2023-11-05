from django import forms
from django.utils import timezone
from categorias.models import Categoria

class FichaForm(forms.Form):
   # Nombre que le dará el usuario a su movimiento
   titulo = forms.CharField(label="Titulo")

   # Dinero el que será sumado o restado al monto final
   monto = forms.CharField(widget=forms.TextInput())

   # Fecha en el que creo el nuevo movimiento
   fecha_creacion = forms.DateField(widget=forms.SelectDateWidget(), initial=timezone.now().strftime("%Y-%m-%d"))

   # Si el movimiento es un egreso o ingreso
   tipo = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=True)

   # Función para que en"monto" no se permita un número 
   # no enteros, y para que sea obligatorio llenarlo.

   """
   def clean_numero(self):
        numero = self.cleaned_data['monto']

        # Si el campo no es llenado o se enviará el form.
        if not numero:
            raise forms.ValidationError('Este campo es obligatorio.')
        
        # Si el numero no es entero no se enviará el form.
        try:
            int(numero)
        except ValueError:
            raise forms.ValidationError('Ingrese un número entero válido.')
        return numero
   """

