
from argparse import Action
from crypt import methods
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action


class PontoTuristicoViewSet(ModelViewSet):
    
    #queryset = PontoTuristico.objects.all() #também poderia passar o argumento aqui
    queryset = PontoTuristico.objects.filter(aprovado = True)
    serializer_class = PontoTuristicoSerializer

    # def get_queryset(self):
    #     return PontoTuristico.objects.filter(aprovado = True)

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste':123})

    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello':request.data['nome']})

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)
   
    # @action(methods=['get'], detail=True)

    # def denunciar(self, request, pk=None):
    #     pass

    # @action(methods=['get'],detail=False)

    # def teste (self, request):
    #     pass