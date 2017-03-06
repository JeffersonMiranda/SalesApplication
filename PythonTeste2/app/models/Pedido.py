from django.db import models
from app.models.TipoPedido import TipoPedido
from app.models.Cliente import Cliente
from app.models.Representacao import Representacao
from app.models.Prazo import Prazo

class Pedido(models.Model):
        
       data_emissao = models.DateTimeField()
       total_faturado = models.DecimalField(null = True, decimal_places = 2, max_digits = 10)
       desconto_geral_porcent = models.DecimalField(null = True, decimal_places = 2, max_digits = 10)
       desconto_geral_valor = models.DecimalField(null = True, decimal_places = 2, max_digits = 10)
       valor_total = models.DecimalField(null = True, decimal_places = 2, max_digits = 10)
       prazo = models.ForeignKey(Prazo) 
       tipo_pedido = models.ForeignKey(TipoPedido)
       status = models.TextField()
       cliente = models.ForeignKey(Cliente)
       representacao = models.ForeignKey(Representacao)
    