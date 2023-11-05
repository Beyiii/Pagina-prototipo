# 2023-1-Grupo-0

A continuación se daran las instrucciones para descargar y correr la aplicación:

## Clonar repositorio

Lo primero que se debe hacer es clonar el repositorio en una carpeta vacia. 

![clonar](https://github.com/DCC-CC4401/2023-1-Grupo-0/assets/81399010/d4ae89b7-af5c-472c-a5ee-3faafa87d2a2)

Se puede hacer copiando la URL y luego en la consola local, dentro de la carpeta vacia (que se debe crear), se escribe:

```
git clone https://github.com/...
```

## Crear el ambiente virtual

Para crear el ambiente, se navega por consola hasta la carpeta en la que se quieras crear y se escribe:

```
python -m venv myvenv
```
El parámetro `-m venv` es para indicar que estamos usando el módulo venv, y `myvenv` es el nombre del ambiente (el nombre puede ser otro, pero sin acento ni con caracteres especiales).

## Activar el ambiente virtual 

La forma de activarlo cambia según el sistema operativo y/o consola. Se navega por la consola hasta la carpeta en que se creó el ambiente virtual y se escribe:

Windows:
```
myvenv\Scripts\activate
```
Linux:
```
source myvenv\bin\activate
```

Una vez activado, en la ruta que indica la consola se debería agregar el nombre del ambiente entre paréntesis. Por ejemplo:

```
(myenv) C:\Documentos\Ingenieria1\Inicio-Proyectos>
```

Ahora que se tiene el entorno virtual iniciado, se puede instalar las dependencias del proyecto, pero antes de eso, se debe asegurar de tener la última versión de pip, el software que se utiliza para instalar Django:
```
(myenv) ~$ python -m pip install --upgrade pip
```

## requirements.txt 

Teniendo activado el ambiente, se navega por la consola hasta la carpeta donde se clonó el repositorio y se escribe:

```
(myenv) pip install -r requirements.txt
```
Esto instalará de una vez todo lo que esté declarado en el archivo.

## Correr el Proyecto

Antes de correr el proyecto descargado, se debe asegurar de encontrar en la carpeta proyecto:

![image](https://github.com/DCC-CC4401/2023-1-Grupo-0/assets/81399010/f1c8cc48-c48d-47fa-9d55-416324710f91)

Para ello, se debe navergar por la consola hasta la carpeta anteriormente mencionada.

Luego, es necesario aplicar la primera capa de migraciones. Para esto hacemos lo siguiente:

```
(myenv) python manage.py makemigrations
        python manage.py migrate
```

Por último, para poder acceder a la aplicación web se debe escribir el siguiente comando:

```
(myenv) python manage.py runserver
```

Al entrar a http://127.0.0.1:8000/ se debería ver lo siguiente:

![image](https://github.com/DCC-CC4401/2023-1-Grupo-0/assets/81399010/23f117d8-ad3b-4a0f-b78b-de54975601d4)









