from rest_framework import viewsets
from imagens.api.serializer import imagensHistoricosSerializer
from imagens.models import imagensHistorico

class imagensHistoricosViewSet(viewsets.ModelViewSet):
    queryset = imagensHistorico.objects.all()
    serializer_class = imagensHistoricosSerializer