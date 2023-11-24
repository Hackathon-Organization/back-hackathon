from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import UserViewSet
from modelagem.views import(
    AvaliadorViewSet,
    EmpresasViewSet,
    EquipesViewSet, 
    HackathonViewSet,
    ParticipantesViewSet,
    ProjetosViewSet,
    TecnologiasViewSet,
)

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register(r"avaliadores", AvaliadorViewSet)
router.register(r"empresas", EmpresasViewSet)
router.register(r"equipes", EquipesViewSet)
router.register(r"hackathon", HackathonViewSet)
router.register(r"participantes", ParticipantesViewSet)
router.register(r"projetos", ProjetosViewSet)
router.register(r"tecnologias", TecnologiasViewSet)

urlpatterns = [
    # API
    path("api/", include(router.urls)),
    # Admin
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Simple JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
