from django.db import models

class sobremim1(models.Model):
    texto1 = models.TextField()
    texto2 = models.TextField()

class dados1(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cell = models.IntegerField()
    bio = models.TextField() 

class foto1(models.Model):
    titulo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto/')

    def __str__(self):
        return self.titulo

