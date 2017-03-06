from django.db import models


class Contato(models.Model):
    """description of class"""
    email = models.EmailField(null = True)
    telefone1 = models.TextField(null = True)
    telefone2 = models.TextField(null = True)
    celular1 = models.TextField(null = True)
    celular2 = models.TextField(null = True)
    site = models.TextField(null = True)
    

