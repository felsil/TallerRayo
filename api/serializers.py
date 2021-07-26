from rest_framework import serializers
from miTaller.models import Reparacion, CategoriaReparacion, Contacto


#creacion de modelo a serializar

class ReparacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reparacion
        fields =["nombreReparacion","descripcionReparacion","imagen"]

class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaReparacion
        fields =["nombreCategoria"]

class ContactoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields =["nombreContacto","apellidoContacto","emailContacto","fonoContacto","mensajeContacto"]