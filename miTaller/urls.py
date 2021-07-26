from django.contrib import admin
from django.urls import path, include
from .views import buscar, contacto, crear_usuario, cerrar_sesion, formulario, index, galeria, eliminar_reparacion, detalle_reparacion, filtro_categoria, filtro_descripcion, login

urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('eliminar_reparacion/<id>/',eliminar_reparacion,name='ELIM'),
    path('detalle/<id>/',detalle_reparacion,name='DR'),
    path('filtro_categoria/',filtro_categoria,name='FILTROCA'),
    path('filtro_descripcion/',filtro_descripcion,name='FILTRODES'),
    path('login/',login,name='LOGIN'),
    path('logout/',cerrar_sesion,name='CERRAR'),
    path('crear_usuario/',crear_usuario,name='CREARUSER'),
    path('contacto/',contacto,name='CONTACTO'),
    path('buscar/<id>/',buscar,name='BUSCAR'),   
  
]