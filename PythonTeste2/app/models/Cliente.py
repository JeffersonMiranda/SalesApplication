from django.db import models
from app.models.Contato import Contato
from app.models.Endereco import Endereco


class Cliente(models.Model):       
     
       cnpj = models.BigIntegerField()
       nome_fantasia = models.TextField()
       razao_social = models.TextField()
       inscri_municipal = models.TextField(null = True)
       inscri_estadual = models.TextField(null = True)
       endereco = models.ForeignKey(Endereco, null = True)# INCLUI BAIRRO, CIDADE E ESTADO
       contato = models.ForeignKey(Contato, null = True)
       status = models.TextField()
   



