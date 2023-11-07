# Django View

from django.http import HttpRequest, HttpResponse
import json

def ping(request):
    response_data = {'message': 'pong'}
    return HttpResponse(json.dumps(response_data), status=200)

