from django.shortcuts import render, redirect, get_object_or_404
from ficha.models import Ficha
from categorias.models import Categoria
from ficha.forms import FichaForm
from usuarios.models import User


# En esta vista, solo se mostrará su contenido al dueño de la ficha (el usuario registrado)
def fichas(request):
    if request.user.is_authenticated:
        mis_fichas = Ficha.objects.filter(owner=request.user) # Obtener todas las fichas del usuario
    else: 
        mis_fichas = Ficha.objects.filter(owner=None)
    
    # Se obtienen todos los objetos 'Categoria' almacenados en la base de datos
    # es decir, los dos tipos movimientos que se permiten "Ingreso" y "Egreso".
    tipo = Categoria.objects.all()  

    monto_total = calculadora(request, mis_fichas) 

    # Se renderiza el form creado (con los campos vacios) y las fichas del usuario 
    if request.method == "GET":
        form_ficha = FichaForm()
        return render(request, "ficha/ingresos_egresos.html", {"fichas": mis_fichas, "form_ficha": form_ficha, "tipo": tipo, "monto_total": monto_total })

    # Se crea una nueva ficha, si es que la información escrita en el formulario es valida
    if request.method == "POST":
        form_ficha = FichaForm(request.POST)
        if form_ficha.is_valid():
            cleaned_data = form_ficha.cleaned_data
            if request.user.is_authenticated:
                Ficha.objects.create(**cleaned_data,owner=request.user)
            else:
                Ficha.objects.create(**cleaned_data)   
        monto_total = calculadora(request, mis_fichas) 
        form_ficha = FichaForm()
        return render(request, "ficha/ingresos_egresos.html", {"fichas": mis_fichas, "form_ficha": form_ficha, "tipo": tipo, "monto_total": monto_total})

def calculadora(request, mis_fichas: Ficha.objects):
    monto_total = 0

    if request.user.is_authenticated:
        mis_fichas = Ficha.objects.filter(owner=request.user) # Obtener todas las fichas del usuario
    else: 
        mis_fichas = Ficha.objects.filter(owner=None)  

    # Calcular el total del monto 
    for ficha in mis_fichas:
        if ficha.tipo == Categoria.objects.get(nombre="Ingreso"):
            string_monto = ficha.monto.replace(",", "")
            monto_total += int(string_monto)

        else:
            string_monto = ficha.monto.replace(",", "")
            monto_total -= int(string_monto) 

    return monto_total


def eliminar_ficha(request, ficha_id):
    if request.method == 'POST':
        try:
            ficha = Ficha.objects.get(id=ficha_id)
            ficha.delete()
            return redirect(request.path)  # Redirecciona a la misma URL actual
        except Ficha.DoesNotExist:
            return render(request,"ficha/ingresos_egresos.html", {'mensaje': 'La ficha no existe.'})
    
    return redirect(request.META.get('HTTP_REFERER', 'ruta_lista_fichas'))

def editar_ficha(request, ficha_id):
    ficha = get_object_or_404(Ficha, pk=ficha_id)

    if request.method == 'POST':
        # Actualizar los detalles de la ficha según los datos enviados en el formulario
        ficha.titulo = request.POST.get('titulo')
        ficha.monto = request.POST.get('monto')
        ficha.save()
        return redirect(request.path)  # Redirecciona a la misma URL actual

    return redirect(request.META.get('HTTP_REFERER', 'ruta_lista_fichas'))

