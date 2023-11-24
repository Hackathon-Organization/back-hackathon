from rest_framework.viewsets import ModelViewSet

from modelagem.models import Equipes
from modelagem.serializers import EquipeSerializers


class EquipesViewSet(ModelViewSet):
    queryset = Equipes.objects.all()
    serializer_class = EquipeSerializers