from rest_framework.serializers import ModelSerializer, SlugRelatedField

from modelagem.models.empresas import Empresa

class EmpresasSerializers(ModelSerializer):
    class Meta: 
        model = Empresa
        fields = "__all__"