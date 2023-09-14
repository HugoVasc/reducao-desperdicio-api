from django.db import models
from accounts.models import Usuario
# from .forms import CEPField

LISTA_ESTADOS = (
    ("df", "DF"),
    ("go", "GO"),
    ("mg", "MG"),
)

# Create your models here.

# tabela Cliente
class Cliente(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    preferencia_org = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
# class Instituicao
class Instituicao(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome_instituicao = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=14, unique=True)
    #cep = CEPField() -> não aparece no admin
    rua = models.CharField(max_length=25)
    complemento = models.CharField(max_length=25)
    bairro = models.CharField(max_length=15)
    estado = models.CharField(max_length=15, choices=LISTA_ESTADOS)
    
    def __str__(self):
        return self.nome_instituicao

# tabela Feira
class Feira(models.Model):
    nome_feira = models.CharField(max_length=50)
    img = models.ImageField(upload_to="img_feiras", default="media/img_feiras/default.jpg")
    #cep = CEPField() -> não aparece no admin
    rua = models.CharField(max_length=25)
    complemento = models.CharField(max_length=25)
    bairro = models.CharField(max_length=15)
    estado = models.CharField(max_length=15, choices=LISTA_ESTADOS)
    
    def __str__(self):
        return self.nome_feira

# tabela Produto
class Produto(models.Model):
    nome_produto = models.CharField(max_length=15)
    descricao = models.TextField(max_length=100)
    qtd = models.CharField(max_length=15)
    organic = models.BooleanField(default=False)
    reservado = models.BooleanField(default=False)
    doador = models.ForeignKey(Instituicao, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
# tabela Feirante
class Feirante(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome_banca = models.CharField(max_length=50)
    bancas = models.ManyToManyField(Feira, related_name='feirantes')
    horario_saida = models.TimeField(null=True, blank=True)
    produtos_disponiveis = models.ManyToManyField(Produto, related_name='feirantes')
    
    def __str__(self):
        return self.nome_banca
    