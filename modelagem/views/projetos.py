from rest_framework.viewsets import ModelViewSet

from modelagem.models import Projetos
from modelagem.serializers import ProjetoSerializers


class ProjetosViewSet(ModelViewSet):
    queryset = Projetos.objects.all()
    serializer_class = ProjetoSerializers