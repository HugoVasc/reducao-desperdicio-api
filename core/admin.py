from django.contrib import admin
from .models import Feira

# Register your models here. (registrar tabelas do db para poderem ser acessadas pelo admin)
admin.site.register(Feira)
