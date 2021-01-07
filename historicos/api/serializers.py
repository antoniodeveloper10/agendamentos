from rest_framework import serializers
from historicos.models import Historicos
from  imagens.api.serializer import imagensHistoricosSerializer

class HistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = '__all__'
class HistoricosDetalhesSerializer(serializers.ModelSerializer):
    imagens = imagensHistoricosSerializer(many=True, read_only=True)
    class Meta:
        model = Historicos
        fields = [
            'id_historico',
            'data',
            'aparecimentos_sintomas' ,
            'duracao_sintomas' ,
            'local_dor' ,
            'tipo_dor',
            'remedios',
            'conclusao',
            'imagens'
        ]