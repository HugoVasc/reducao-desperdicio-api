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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

# to do
class DescricaoProdutos(DetailView):
    pass

# to do
class EditarProdutos(TemplateView):
    pass
