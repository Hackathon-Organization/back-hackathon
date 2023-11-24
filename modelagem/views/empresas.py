from rest_framework.viewsets import ModelViewSet

from modelagem.models.empresas import Empresa
from modelagem.serializers.empresas import EmpresasSerializers


class EmpresasViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresasSerializers