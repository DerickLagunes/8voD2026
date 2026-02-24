from django.urls import path

from core import views as core
from mascota_api import views as mascotas

urlpatterns = [
   #path para la página raiz == index = home == inicio
   path('', core.index, name='index'),
   path('contacto/', core.contacto, name='contacto'),
   path('onepage/', core.onepage, name='onepage'),
   path('derick/', core.derick, name='derick'),
   path('ruben/', core.ruben, name='ruben'),
   path('alexandro', core.alexandro, name='alexandro'),
   path('OscarMontesCV', core.OscarMontesCV, name='OscarMontesCV'),
   path('cvjona/', core.cvjona, name='cvjona'),
   path('cisco/', core.cisco, name='cisco'),
   path('luis-ricardo-medina-villagomez', core.cv, name='cv'),
   path('Alison/', core.Alison, name='Alison'),

   path('mascotas/', mascotas.api_lista_mascotas, name='lista_mascotas'),
    path('mascotas/nueva/', mascotas.api_crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:pk>/', mascotas.api_editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:pk>/', mascotas.api_eliminar_mascota, name='eliminar_mascota'),

]
