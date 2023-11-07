from django.http import JsonResponse
from django.conf import settings

PRE_SHARED_SECRET = 'your_secret_key'  # Replace with your actual secret key

def authenticate_with_shared_secret(view_func):
    def wrapped_view(request, *args, **kwargs):
        header_secret = request.META.get('HTTP_X_SHARED_SECRET')
        if header_secret != settings.PRE_SHARED_SECRET:
            return JsonResponse({'error': 'Unauthorized'}, status=401)
        return view_func(request, *args, **kwargs)
    return wrapped_view


@authenticate_with_shared_secret
def protected_view(request):
    return JsonResponse({'message': 'Authorized'})

