from rest_framework.serializers import ModelSerializer, SlugRelatedField

from modelagem.models import Projetos

class ProjetoSerializers(ModelSerializer):
    class Meta: 
        model = Projetos
        fields = "__all__"