#O SERIALIZER CONVERTE DE PYTHON P JSON E VICE-VERSA pq a linguagem da api é JSON

from rest_framework import serializers

#importando todas as classes do model
from .models import *

class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        #converte de uma vez só vários usuários e retorna em um ARRAY
        many = True
        #recebe o modelo da tabela Usuarios para converter
        model = Usuarios
        #recebe todos os campos da classe
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Categoria
        fields = '__all__'

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Filmes
        fields = '__all__'

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Assinatura
        fields = '__all__'

class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Favoritos
        fields = '__all__'