from rest_framework.viewsets import ModelViewSet

from modelagem.models import Hackathon
from modelagem.serializers import HackathonSerializers


class HackathonViewSet(ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializers