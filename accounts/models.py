from django.db import models
from django.db.models import Count

class Person(models.Model):
    """Person model"""
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=14, unique=True)
    data_nasc = models.DateField()
    sexo = models.CharField(max_length=10)
    mae = models.CharField(max_length=120)
    pai = models.CharField(max_length=120)
    celular = models.CharField(max_length=20)
    altura = models.FloatField()
    peso = models.FloatField()
    tipo_sanguineo = models.CharField(max_length=4)

    def __str__(self):
        return self.nome
    
    @classmethod
    def gen_frequency(cls, key):
        """Returns the frequency of an attribute"""
        freq = cls.objects.values(key)
        freq = freq.annotate(Count(key))
        freq = [{fi[key]: fi[f'{key}__count']} for fi in freq]
        freq = {key: value for dict_ in freq for key, value in dict_.items()}
        return freq

    @classmethod
    def gen_distribution(cls, key):
        """Returns the distribution of an attribute"""
        dist = cls.gen_frequency(key)
        acc = sum(dist.values())
        dist = {key: value / acc for key, value in dist.items()}
        return dist