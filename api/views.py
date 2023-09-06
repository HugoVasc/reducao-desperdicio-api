from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# from django.shortcuts import render
from .serializers import FeiraSerializer, ClienteSerializer, InstituicaoSerializer, ProdutoSerializer, FeiranteSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def feira(request):
    if request.method == 'GET':
        feiras = FeiraSerializer.Meta.model.objects.all()
        serializer = FeiraSerializer(feiras, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = FeiraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def produto(request):
    if request.method == 'GET':
        produtos = ProdutoSerializer.Meta.model.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = ProdutoSerializer(data=request.data)
        try:
            produto = ProdutoSerializer.Meta.model.objects.get(id=serializer.data['id_produto'])
            if serializer.is_valid():
                produto.nome_produto = serializer.data['nome_produto']
                produto.descricao = serializer.data['descricao']
                produto.qtd = serializer.data['qtd']
                produto.organic = serializer.data['organic']
                produto.reservado = serializer.data['reservado']
                produto.doador = serializer.data['doador']
                produto.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ProdutoSerializer.Meta.model.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        serializer = ProdutoSerializer(data=request.data)
        try:
            produto = ProdutoSerializer.Meta.model.objects.get(id=serializer.data['id_produto'])
            if serializer.is_valid():
                produto.delete()
                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT, data={"message": "Produto deletado com sucesso!"})
        except ProdutoSerializer.Meta.model.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def cliente(request):
    if request.method == 'GET':
        clientes = ClienteSerializer.Meta.model.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
