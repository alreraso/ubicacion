from django.shortcuts import render
# Create your views here.
from direccion.models import Direccion
from direccion.serializer import DireccionSerializer
from rest_framework import mixins
from rest_framework import generics
from django_filters import rest_framework as filtros
from rest_framework import filters
from url_filter.integrations.drf import DjangoFilterBackend
class DireccionList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):

    """ 
    Codigo de peticiones generico para las vistas

    Parameters:
        *args    
            Lista de argumentos de longitud variable.
        **kwargs
            Argumentos con plabras claves arbitrarias.
    """

    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DireccionDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    
    """ 
    Codigo de peticiones generico para las vistas

    Parameters:
        *args    
            Lista de argumentos de longitud variable.
        **kwargs
            Argumentos con plabras claves arbitrarias.
    """

    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)