from django.contrib import admin

from planeyarium.models import (
    ShowTheme,
    AstronomyShow,
    ShowSession,
    PlanetariumDome,
    Ticket,
    Reservation,
)

admin.site.register(ShowTheme)
admin.site.register(AstronomyShow)
admin.site.register(PlanetariumDome)
admin.site.register(ShowSession)
admin.site.register(Reservation)
admin.site.register(Ticket)


