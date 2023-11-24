from django.db import models

class Hackathon(models.Model):
    class Meta:
        verbose_name = "Hackathon"
        verbose_name_plural = "Hackathon"
        
    nome = models.CharField(max_length=50) 
    data_inicio = models.DateField( )
    data_final = models.DateField( )
    equipe = models.CharField(max_length=50)
    jurados = models.CharField(max_length=50)