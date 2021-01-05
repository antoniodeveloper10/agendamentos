from rest_framework import viewsets
from pacientes.models import Pacientes
from pacientes.api.serializers import PacientesSerializer

class PacientesViewSet(viewsets.ModelViewSet):
    """ Exibir todos Pacientes """
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    