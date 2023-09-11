from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from planeyarium.models import (
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    ShowTheme,
)
from planeyarium.serializers import AstronomyShowListSerializer, AstronomyShowDetailSerializer


ASTRONOMY_SHOW_URL = reverse("planeyarium:astronomy_show-list")


def sample_astronomy_show(**params):
    defaults = {
        "title": "Sample astronomy show",
        "description": "Sample description"
    }
    defaults.update(params)

    return AstronomyShow.objects.create(**defaults)


def sample_theme(**params):
    defaults = {
        "name": "Solar system",
    }
    defaults.update(params)

    return ShowTheme.objects.create(**defaults)


def sample_show_session(**params):
    planetarium_dome = PlanetariumDome.objects.create(
        name="Gemini", rows=20, seats_in_row=20
    )
    astronomy_show = sample_astronomy_show()

    defaults = {
        "show_time": "2024-06-02 14:00:00",
        "astronomy_show": astronomy_show,
        "planetarium_dome": planetarium_dome,
    }
    defaults.update(params)

    return ShowSession.objects.create(**defaults)


def detail_url(astronomy_show_id):
    return reverse("planetarium:astronomy_show-detail", args=[astronomy_show_id])


class UnauthenticatedAstronomyShowApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_authentication_required(self):
        res = self.client.get(ASTRONOMY_SHOW_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedAstronomyShowApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test.com", password="testpassword"
        )
        self.client.force_authenticate(self.user)

    def test_list_astronomy_show(self):
        sample_astronomy_show()
        astronomy_show_with_theme = sample_astronomy_show()
        theme = sample_theme()

        astronomy_show_with_theme.show_themes.add(theme)

        res = self.client.get(ASTRONOMY_SHOW_URL)

        astronomy_shows = AstronomyShow.objects.all()
        serializer = AstronomyShowListSerializer(astronomy_shows, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_astronomy_show_filter_by_title(self):
        astronomy_show1 = sample_astronomy_show(title="Testik1")
        astronomy_show2 = sample_astronomy_show(title="Testik2")
        astronomy_show3 = sample_astronomy_show(title="Test3")

        res = self.client.get(ASTRONOMY_SHOW_URL, {"title": "Testik"})

        serializer1 = AstronomyShowListSerializer(astronomy_show1)
        serializer2 = AstronomyShowListSerializer(astronomy_show2)
        serializer3 = AstronomyShowListSerializer(astronomy_show3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_astronomy_show_filter_by_themes(self):
        astronomy_show1 = sample_astronomy_show(title="Testik1")
        astronomy_show2 = sample_astronomy_show(title="Testik2")
        astronomy_show3 = sample_astronomy_show(title="Test3")

        theme1 = sample_theme(name="test_theme1")
        theme2 = sample_theme(name="test_theme2")

        astronomy_show1.show_themes.add(theme1)
        astronomy_show2.show_themes.add(theme2)

        res = self.client.get(ASTRONOMY_SHOW_URL,{"show_themes": f"{theme1.id},{theme2.id}"})

        serializer1 = AstronomyShowListSerializer(astronomy_show1)
        serializer2 = AstronomyShowListSerializer(astronomy_show2)
        serializer3 = AstronomyShowListSerializer(astronomy_show3)

        self.assertIn(serializer1.data, res.data)
        self.assertIn(serializer2.data, res.data)
        self.assertNotIn(serializer3.data, res.data)

    def test_retrieve_astronomy_show_detail(self):
        astronomy_show = sample_astronomy_show()

        url = detail_url(astronomy_show.id)
        res = self.client.get(url)

        serializer = AstronomyShowDetailSerializer(astronomy_show)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_astronomy_show_forbidden(self):
        payload = {
            "title": "AstronomyShow",
            "description": "AstronomyShow description",
        }
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminAstronomyShowApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="admintest@test.com", password="admintestpassword", is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_astronomy_show(self):
        payload = {
            "title": "Test astronomy show",
            "description": "Test description",
        }

        res = self.client.post(ASTRONOMY_SHOW_URL, payload)

        astronomy_show = AstronomyShow.objects.get(id=res.data["id"])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        for key in payload:
            self.assertEqual(payload[key], getattr(astronomy_show, key))

    def test_delete_astronomy_show_not_allowed(self):
        astronomy_show = sample_astronomy_show()
        url = detail_url(astronomy_show.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
