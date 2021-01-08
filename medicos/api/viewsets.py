from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from medicos.api.serializer import MedicosSerializer,MedicosDetalhesSerializer
from medicos.models import Medicos

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class =MedicosSerializer

    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    
    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Medicos.objects.filter(pk=pk)
        self.serializer_class = MedicosDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)