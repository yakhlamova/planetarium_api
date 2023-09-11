from django.urls import path, include
from rest_framework import routers
from django.conf import settings

from planeyarium.views import (
    ShowThemeViewSet,
    AstromyShowViewSet,
    ShowSessionViewSet,
    PlanetariumDomeViewSet,
    ReservationViewSet,
)

app_name = "planeyarium"

router = routers.DefaultRouter()
router.register("show_themes", ShowThemeViewSet)
router.register("astronomy_shows", AstromyShowViewSet)
router.register("planetarium_domes", PlanetariumDomeViewSet)
router.register("show_sessions", ShowSessionViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]
