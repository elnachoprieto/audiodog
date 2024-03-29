from django.urls import path
from . import views

urlpatterns = [
    path('', views.cancion_list, name='cancion_list'),
    path('usuario_registro/', views.usuario_registro, name='usuario_registro'),
    path('usuario_guardar/', views.usuario_guardar, name='usuario_guardar'),
    path('usuario_eliminar/', views.usuario_eliminar, name='usuario_eliminar'),
    path('ciudad_get/', views.ciudad_get, name='ciudad_get'),
    path('cancion_subir/', views.cancion_subir, name='cancion_subir'),
    path('cancion_guardar/', views.cancion_guardar, name='cancion_guardar'),
]
