from django.db import models
from app.models.Pedido import Pedido


class Comissao(models.Model):
     
         porcentagem = models.DecimalField(null = False, decimal_places = 2, max_digits=4)
         valor = models.DecimalField(null = False, decimal_places = 2, max_digits = 10 )
         pedido = models.OneToOneField(Pedido)
         


