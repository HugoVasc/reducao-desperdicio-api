from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# from django.shortcuts import render
from .serializers import FeiraSerializer, ClienteSerializer, InstituicaoSerializer, ProdutoSerializer, FeiranteSerializer
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"
    
class Cadastro(TemplateView):
    template_name = "cadastro.html"
    
class CadastroFeirante(TemplateView):
    template_name = "cadastro_feirante.html"
    
class CadastroInstituicao(TemplateView):
    template_name = "cadastro_instituicao.html"
    
class CadastroCliente(TemplateView):
    template_name = "cadastro_cliente.html"
    
class Filtro(TemplateView):
    template_name = "filtro.html"
    
class Mapa(TemplateView):
    template_name = "mapa.html"
    
class Ofertas(ListView):
    template_name = "oferta_produtos.html"
    #model =

class Doacoes(TemplateView):
    template_name = "doacoes.html"
    
class Sobras(TemplateView):
    template_name = "sobras.html"
    
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


# to do
class DescricaoProdutos(DetailView):
    pass

# to do
class EditarProdutos(TemplateView):
    pass
