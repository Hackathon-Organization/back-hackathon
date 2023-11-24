from rest_framework.viewsets import ModelViewSet
from core.models import User
from core.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')  # Adicione a ordenação por 'id' ou outro campo apropriado
    serializer_class = UserSerializer

    