from django.db import models
from app.models.Endereco import Endereco
from app.models.Contato import Contato


class Representacao(models.Model):
          
            
        cnpj = models.BigIntegerField(null = True)
        nome_fantasia = models.TextField()
        razao_social = models.TextField()
        inscri_estadual = models.TextField(null = True)
        endereco = models.ForeignKey(Endereco, null = True)  # INCLUI BAIRRO, CIDADE E ESTADO
        contato = models.ForeignKey(Contato, null = True)


