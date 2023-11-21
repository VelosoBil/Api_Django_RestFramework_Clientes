from django.db import models


class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    endereco = models.CharField(max_length=100, null=False)
    bairro = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    uf = models.CharField(max_length=2, null=False)
    celular = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome, self.endereco, self.bairro, self.uf, self.celular