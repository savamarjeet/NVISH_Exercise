from django.urls import reverse
import json

def test_ping_view(client):
    url = reverse('ping')
    response = client.get(url)

    assert response.status_code == 200
    response_data = json.loads(response.content.decode('utf-8'))
    assert response_data['message'] == 'pong'
