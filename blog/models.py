from django.db import models

class sobremim1(models.Model):
    texto1 = models.TextField()
    texto2 = models.TextField()

class dados1(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cell = models.IntegerField()
    bio = models.TextField() 

