from django.db import models

class Estado(models.Model):
    
     id = models.IntegerField(primary_key=True)    
     uf = models.CharField(max_length = 2)
     nome = models.TextField()

