
from django.db import models
from app.models.Contato import Contato
from app.models.Cliente import Cliente

class VendedorDoCliente(models.Model):
  
         nome = models.TextField()
         contato = models.ForeignKey(Contato)
         cliente = models.ForeignKey(Cliente)


