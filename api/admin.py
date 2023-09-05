from django.contrib import admin
from .models import Usuario, Cliente, Instituicao, Feira, Produto, Feirante
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Usuario, UserAdmin) # usar usuario personalizado
admin.site.register(Cliente)
admin.site.register(Instituicao)
admin.site.register(Feira)
admin.site.register(Produto)
admin.site.register(Feirante)