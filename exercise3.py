from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import KeyValue

def save(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        if key and value:
            KeyValue.objects.create(key=key, value=value)
            return JsonResponse({'message': 'Data saved successfully'})
        else:
            return JsonResponse({'error': 'Key and value are required'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get(request, key):
    if request.method == 'GET':
        try:
            data = KeyValue.objects.get(key=key)
        except KeyValue.DoesNotExist:
            return JsonResponse({'error': 'Requested key Does not Exist'}, status=400)
        return JsonResponse({'key': data.key, 'value': data.value}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def delete(request, key):
    if request.method == 'DELETE':
        try:
            data = KeyValue.objects.get(key=key)
        except KeyValue.DoesNotExist:
            return JsonResponse({'error': 'Requested key Does not Exist'}, status=400)
        data.delete()
        return JsonResponse({'message': 'Data deleted successfully'})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
