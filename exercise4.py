from django.http import JsonResponse
from .models import KeyValue
from django.core.cache import cache

def save(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        if key and value:
            KeyValue.objects.create(key=key, value=value)
            # Save to cache for 5 minutes
            cache.set(key, value, 300)  # 300 seconds
            return JsonResponse({'message': 'Data saved successfully'})
        else:
            return JsonResponse({'error': 'Key and value are required'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get(request, key):
    if request.method == 'GET':
        # Try to retrieve the data from the cache
        value = cache.get(key)
        if value is not None:
            return JsonResponse({'key': key, 'value': value})
        # If not found in the cache, query the database
        try:
            data = KeyValue.objects.get(key=key)
        except KeyValue.DoesNotExist:
            return JsonResponse({'error': 'Requested key Does not Exist'}, status=400)
        # Store the result in the cache for future use. Save to cache for 5 minutes/300 seconds
        cache.set(key, data.value, 300)
        return JsonResponse({'key': data.key, 'value': data.value}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
