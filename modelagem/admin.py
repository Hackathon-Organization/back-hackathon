from django.contrib import admin

from .models import Hackathon, Participantes, Equipes, Projetos

admin.site.register(Hackathon)
admin.site.register(Participantes)
admin.site.register(Equipes)
admin.site.register(Projetos)