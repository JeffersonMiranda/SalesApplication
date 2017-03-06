from django.db import models
from app.models.Cidade import Cidade
from app.models.Estado import Estado

class Endereco(models.Model):
   
     rua = models.TextField(null = True)
     numero = models.TextField(null = True)
     referencia = models.TextField(null = True)
     cep = models.BigIntegerField(null = True)
     bairro = models.TextField(null = True)
     cidade = models.ForeignKey(Cidade,null = True)
     estado = models.ForeignKey(Estado,null = True)

     

