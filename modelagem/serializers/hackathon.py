from rest_framework.serializers import ModelSerializer, SlugRelatedField

from modelagem.models import Hackathon

class HackathonSerializers(ModelSerializer):
    class Meta: 
        model = Hackathon
        fields = "__all__"