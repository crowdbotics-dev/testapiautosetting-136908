from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136908ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136908", Testconnectors136908ViewSet, basename="testconnectors136908"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
