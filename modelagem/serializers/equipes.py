from rest_framework.serializers import ModelSerializer, SlugRelatedField

from modelagem.models import Equipes

class EquipeSerializers(ModelSerializer):
    class Meta: 
        model = Equipes
        fields = "__all__"