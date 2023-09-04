from django.urls import path, include
from .views import Homepage, Cadastro, CadastroFeirante, CadastroInstituicao, CadastroCliente, Filtro, Mapa, Ofertas, Doacoes, Sobras, feira, produto


urlpatterns = [
    path('', Homepage.as_view()),
    path('cadastro/', Cadastro.as_view()),
    path('cadastro/feirante', CadastroFeirante.as_view()),
    path('cadastro/instituicao', CadastroInstituicao.as_view()),
    path('cadastro/cliente', CadastroCliente.as_view()),
    path('cliente', Filtro.as_view()),
    path('cliente/feiras', Mapa.as_view()),
    path('cliente/ofertas', Ofertas.as_view()),
    path('instituicao/doacao', Doacoes.as_view()),
    path('feirante/sobras', Sobras.as_view()),
    path('feira', feira),
    path('produto', produto),
]
