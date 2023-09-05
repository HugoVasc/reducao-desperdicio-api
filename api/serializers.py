from rest_framework import serializers
from api import models

class FeiraSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Feira
    fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Cliente
    fields = '__all__'

class InstituicaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Instituicao
    fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Produto
    fields = '__all__'

class FeiranteSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Feirante
    fields = '__all__'