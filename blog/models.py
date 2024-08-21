from django.db import models

class sobremim(models.Model):
    cursos = models.TextField()
    interesses = models.TextField()
    gostos = models.TextField()
    qualidade = models.TextField()

class dados(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    dn = models.DateField()
    altura = models.IntegerField()
    peso = models.IntegerField() 
