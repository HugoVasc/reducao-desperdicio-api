from django.shortcuts import render
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
    
# to do
class DescricaoProdutos(DetailView):
    pass

# to do
class EditarProdutos(TemplateView):
    pass