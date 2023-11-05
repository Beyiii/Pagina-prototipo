from django.urls import include, path
from . import views

urlpatterns = [
    path('login',views.login_user, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('inicio', views.register_user, name='inicio'), 
    path('', include('ficha.urls')),
]