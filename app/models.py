from django.db import models

# Create your models here.

class Usuarios(models.Model):

    nome = models.CharField(max_length=55)

    email = models.CharField(max_length=80)

    fone = models.CharField(max_length=15, default='Não Informado', null=True, blank=True)

    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return  self.nome

class Filmes(models.Model):
    nome = models.CharField(max_length=55)
    categoria = models.ForeignKey(Categoria, default='', on_delete=models.CASCADE)

    def __str__(self):
        return  self.nome

class Assinatura(models.Model):
    nome = models.CharField(max_length=55)
    valor = models.DecimalField(max_digits=5,decimal_places=2)
    def __str__(self):
        return  self.nome

class Favoritos(models.Model):
    filme_id = models.ForeignKey(Filmes, default='', on_delete=models.CASCADE)
    users_id = models.ForeignKey(Usuarios, default='', on_delete=models.CASCADE)