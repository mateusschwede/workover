from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cafeteria(models.Model):
    nome = models.CharField(max_length=255)
    data_inauguracao = models.DateField()
    endereco = models.CharField(max_length=255)
    avaliacao = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])

    def __str__(self):
        return f"{self.nome} ({self.avaliacao}/10)"