import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Note

client = APIClient()

@pytest.fixture
def create_note():
    return Note.objects.create(title='Test Note', body='This is a test note.')


@pytest.mark.django_db
def test_create_note():

    url = "/api/create-note"
    data = {'title': 'Integration Test', 'body': 'This is an integration test note.'}
    response = client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == 'Integration Test'


@pytest.mark.django_db
def test_fetch_note_by_id( create_note):

    url = f'/api/note/{create_note.pk}'
    response = client.get(url, format='json')
    
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == create_note.title
    


@pytest.mark.django_db
def test_query_notes_by_title( create_note):
    
    url = '/api/search-notes?title=Test'
    response = client.get(url, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['title'] == create_note.title
    



@pytest.mark.django_db
def test_update_note( create_note):
    
    url = f'/api/update-note/{create_note.pk}'
    data = {'title': 'Updated Note', 'body': 'Updated content.'}
    response = client.put(url, data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Updated Note'
    assert response.data['body'] == 'Updated content.'


