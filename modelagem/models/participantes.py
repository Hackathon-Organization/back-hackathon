from django.db import models

class Participantes(models.Model):
    class Meta:
        verbose_name = "Particiante"
        verbose_name_plural = "Participantes"
        
    email = models.EmailField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    equipe_atual = models.CharField(max_length=50)
    pontuacao = models.DecimalField(max_digits=10, decimal_places=1, verbose_name = "pontuação", default=0)
    
    def __str__(self):
        return f"({self.nome}) - {self.equipe_atual}"