from rest_framework import serializers
from medicos.models import Medicos
from agendamentos.api.serializers import AgendamentosDetalhesSerializer

class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'

class MedicosDetalhesSerializer(serializers.ModelSerializer):
    agendamentosMedicos = AgendamentosDetalhesSerializer(many=True, read_only=True)
    class Meta:
        model = Medicos
        fields = [
            'id_medico',
            'nome',
            'especialidade',
            'agendamentosMedicos'
        ]


