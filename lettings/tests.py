import pytest
from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
from .models import Address, Letting


@pytest.fixture
def client():
    return Client()


@pytest.mark.django_db
def test_index(client):
    url = reverse("lettings:index")
    response = client.get(url)

    content = response.content.decode()
    expected_content = "<title>Lettings</title>"

    assert response.status_code == 200
    assert expected_content in content


@pytest.mark.django_db
def test_lettings():
    client = Client()

    adress = Address.objects.create(
        number=1,
        street="sesame street",
        city="Los Angeles",
        state="LA",
        zip_code=75012,
        country_iso_code="USA",
    )
    Letting.objects.create(title="Beautifull place", address=adress)
    path = reverse("lettings:lettings", kwargs={"letting_id": 1})
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<title>Beautifull place</title>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")