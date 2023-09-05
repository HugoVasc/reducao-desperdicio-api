from django.urls import path, include
from .views import feira, produto


urlpatterns = [
    path('feira', feira),
    path('produto', produto),
]
