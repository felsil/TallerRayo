from django.shortcuts import render

from rest_framework import generics
from miTaller.models import Reparacion, CategoriaReparacion, Contacto
from .serializers import ReparacionSerializers, CategoriaSerializers, ContactoSerializers


# Create your views here.
class ReparacionesViewSet(generics.ListAPIView):
    queryset = Reparacion.objects.all()
    serializer_class = ReparacionSerializers

class CategoriasViewSet(generics.ListAPIView):
    queryset = CategoriaReparacion.objects.all()
    serializer_class = CategoriaSerializers

class ContactoViewSet(generics.ListAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializers