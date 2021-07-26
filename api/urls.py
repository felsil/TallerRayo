from django.conf.urls import url
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReparacionesViewSet, CategoriasViewSet, ContactoViewSet


urlpatterns=[
    url(r'^api/reparaciones/$',ReparacionesViewSet.as_view()),
    url(r'^api/categoria/$',CategoriasViewSet.as_view()),
    url(r'^api/contacto/$',ContactoViewSet.as_view()),
]
