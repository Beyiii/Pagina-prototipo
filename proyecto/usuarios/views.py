from django.shortcuts import render
from usuarios.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout

# Vista del registro de usuarios
def register_user(request):
   if request.method == 'GET': #Si estamos cargando la página
      return render(request,"usuarios/inicio.html") #Mostrar el template
   
   elif request.method == 'POST': #Si estamos recibiendo el form de registro
      #Se toman los elementos del formulario que vienen en request.POST
      nombre = request.POST['nombre']
      contraseña = request.POST['contraseña']
      apodo = request.POST['apodo']
      pronombre = request.POST['pronombre']
      mail = request.POST['mail']

      #Crear el nuevo usuario
      user = User.objects.create_user(username=nombre, password=contraseña, email=mail, apodo=apodo, pronombre=pronombre)

      #Redireccionar a la página de inicio de sesión
      return HttpResponseRedirect('/login')
   
# Vista del inicio de sesion
def login_user(request):
    if request.method == 'GET':
        return render(request,"usuarios/login.html") # Se Muestra el template
    if request.method == 'POST': # Si se llenan los campos de inicio de sesión
        username = request.POST['username']
        contraseña = request.POST['contraseña']
        usuario = authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/fichas') # Se redirecciona a las fichas (movimientos) del usuario que inició sesión
        else:
            return HttpResponseRedirect('/inicio') # Se redirecciona a la página de inicio ya que el usuario no existe

# Vista al cerrar sesión
def logout_user(request):
   logout(request)
   return HttpResponseRedirect('/inicio') # Se redirecciona a la página de inicio