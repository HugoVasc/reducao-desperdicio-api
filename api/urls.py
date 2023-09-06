from django.urls import path, include
from .views import feira, produto, cliente


urlpatterns = [
    path('feira', feira),
    path('produto', produto),
    path('cliente', cliente),
]
