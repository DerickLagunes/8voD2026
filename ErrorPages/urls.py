from django.urls import path, include

from core import views as core
from registro import views as registro
from error_reports import views as error_reports

urlpatterns = [
   #path para la página raiz == index = home == inicio
   path('', core.index, name='index'),
   path('contacto/', core.contacto, name='contacto'),
   path('onepage/', core.onepage, name='onepage'),
   path('derick/', core.derick, name='derick'),
   path('daniel/', core.daniel, name='daniel'),
   path('formulario/', core.contacto_view, name='formulario'),
   path('registro/', registro.registro_view, name='registro'),
   path('reportes-error/', error_reports.error_reports_view, name='reportes-error'),
   path('obtener-reportes/', error_reports.obtener_reportes, name='obtener-reportes'),
   path('', include('libro_rest.urls')),
]
