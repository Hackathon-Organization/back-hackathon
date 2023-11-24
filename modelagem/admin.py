from django.contrib import admin

from .models import Hackathon, Participantes, Equipes, Projetos, Tecnologias, Empresa, Avaliador

admin.site.register(Avaliador)
admin.site.register(Empresa)
admin.site.register(Hackathon)
admin.site.register(Participantes)
admin.site.register(Equipes)
admin.site.register(Tecnologias)
admin.site.register(Projetos)