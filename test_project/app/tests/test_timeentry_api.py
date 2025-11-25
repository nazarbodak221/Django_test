import pytest

from rest_framework.test import APIClient

from django.urls import reverse

from app.models import TimeEntry

@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_timeentry(api_client):
    url=reverse("timeentry-list")
    data={
        "project_name": "Test Project",
        "description": "Worked on testing",
        "hours": 2.5
    }
    response=api_client.post(url, data, format="json")
    assert response.status_code==201
    assert TimeEntry.objects.count()==1
    assert TimeEntry.objects.first().project_name=="Test Project"