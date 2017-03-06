from django.db import models
from app.models.Produto import Produto


class ItemPedido(models.Model):
     
          produto = models.ForeignKey(Produto)
          quantidade = models.IntegerField()
          desconto_porcentagem = models.DecimalField(max_digits = 10, decimal_places = 2)
          desconto_valor = models.DecimalField(max_digits = 10, decimal_places = 2)
          preco = models.DecimalField(max_digits = 10, decimal_places = 2)
     


