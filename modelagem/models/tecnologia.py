from django.db import models

class Tecnologias(models.Model):
    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"

    nome = models.CharField(max_length=50)
    descrição = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome