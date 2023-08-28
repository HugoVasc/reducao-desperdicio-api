from django.db import models
from .forms import CEPField

# tipos possíveis de feiras
LISTA_TIPOS = (
    ("organico", "Orgânico"),
    ("nao organico", "Não Orgânico")
)

LISTA_ESTADOS = (
    ("df", "Distrito Federal"),
    ("go", "Goiás"),
    ("mg", "Minas Gerais"),
)

# Create your models here (tabelas do banco de dados)

# tabela feiras
class Feira(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15, choices=LISTA_TIPOS)
    img = models.ImageField(upload_to="img_feiras", default="media/img_feiras/default.jpg")
    #cep = CEPField() -> não aparece no admin
    rua = models.CharField(max_length=25)
    complemento = models.CharField(max_length=25)
    bairro = models.CharField(max_length=15)
    estado = models.CharField(max_length=15, choices=LISTA_ESTADOS)
    
    def __str__(self):
        return self.nome
    
    