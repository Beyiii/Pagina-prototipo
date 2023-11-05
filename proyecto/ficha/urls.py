from django.urls import path
from . import views

urlpatterns = [
    path('fichas', views.fichas, name='mis_fichas'), 
    path('eliminar-ficha/<int:ficha_id>/', views.eliminar_ficha, name='eliminar_ficha'),
    path('editar_ficha/<int:ficha_id>/', views.editar_ficha, name='editar_ficha'),
]