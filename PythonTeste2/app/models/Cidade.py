from django.db import models
from app.models.Estado import Estado


class Cidade(models.Model):
    

    id = models.IntegerField(primary_key=True) 
    estado = models.ForeignKey(Estado, null = False)
    nome = models.TextField()

