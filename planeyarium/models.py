from django.conf import settings
from django.db import models


class ShowTheme(models.Model):
    name = models.CharField(max_length=255)


class AstronomyShow(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    show_theme = models.ManyToManyField(ShowTheme)


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(AstronomyShow, related_name="sessions", on_delete=models.CASCADE)
    planetarium_dome = models.ForeignKey(PlanetariumDome, related_name="sessions", on_delete=models.CASCADE)
    show_time = models.DateTimeField()


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )


class Ticket(models.Model):
    movie_session = models.ForeignKey(
        ShowSession, on_delete=models.CASCADE, related_name="tickets"
    )
    order = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name="tickets"
    )
    row = models.IntegerField()
    seat = models.IntegerField()

