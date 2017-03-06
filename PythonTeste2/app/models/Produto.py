
from django.db import models
from app.models.Representacao import Representacao


class Produto(models.Model):
    
    nome = models.TextField()
    preco1 = models.DecimalField(null = True, decimal_places = 2, max_digits = 10)
    preco2 = models.DecimalField(null = True, decimal_places = 2, max_digits = 10)
    preco3 = models.DecimalField(null = True, decimal_places = 2, max_digits = 10)
    status = models.TextField()
    representacao = models.ForeignKey(Representacao)


    



