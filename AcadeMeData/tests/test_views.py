from django.template.loader import render_to_string
import pytest


@pytest.mark.django_db
def test_homepage_html(client):
    response = client.get('')
    assert response.content.decode() == render_to_string('landing/homepage.html')


@pytest.mark.django_db
def test_contactus_html(client):
    response = client.get('/contact_us/')
    assert response.content.decode() == render_to_string('landing/contact_us.html')
