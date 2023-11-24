from django.db import models

class Projetos(models.Model):
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)
    pontuacao = models.DecimalField(max_digits=10, decimal_places=1, verbose_name = "pontuação")
    
    def __str__(self):
        return f"({self.nome}) - {self.pontuacao}"