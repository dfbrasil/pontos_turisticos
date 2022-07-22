
from argparse import Action
from crypt import methods
from urllib import request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter



class PontoTuristicoViewSet(ModelViewSet):
    
    #queryset = PontoTuristico.objects.all() #também poderia passar o argumento aqui
    #queryset = PontoTuristico.objects.filter(aprovado = True)
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['nome','descricao','endereco__linha1']
    #lookup_field = 'nome' está comentado pois pode dar erro se tiver mais de um retorno

    def get_queryset(self):
        id=self.request.query_params.get('id',None)
        nome=self.request.query_params.get('nome',None)
        descricao=self.request.query_params.get('descricao',None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(id=id)
        
        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
        # return PontoTuristico.objects.filter(aprovado = True)

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
   
    # @action(methods=['get'], detail=True)

    # def denunciar(self, request, pk=None):
    #     pass

    # @action(methods=['get'],detail=False)

    # def teste (self, request):
    #     pass