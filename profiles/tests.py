import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from .models import Profile
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_index(client):
    url = reverse("profiles:index")
    response = client.get(url)
    content = response.content.decode()
    expected_content = "<title>Profiles</title>"

    assert response.status_code == 200
    assert expected_content in content


@pytest.mark.django_db
def test_profiles():
    client = Client()

    user = User.objects.create_user(
        username="test_username",
        email="test@gmail.com",
        password="password",
    )
    Profile.objects.create(user=user, favorite_city="Paris")
    path = reverse("profiles:profile", kwargs={"username": user.username})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>test_username</title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")