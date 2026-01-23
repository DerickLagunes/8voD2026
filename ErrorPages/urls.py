from django.urls import path

from core import views as core

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
]
