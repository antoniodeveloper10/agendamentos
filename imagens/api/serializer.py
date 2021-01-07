from rest_framework import serializers
from imagens.models import imagensHistorico


class imagensHistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = imagensHistorico
        fields = '__all__'