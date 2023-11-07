## Django URL
from django.urls import path
from exercise1 import ping
from exercise2 import protected_view
from exercise3 import save, get, delete

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('protected/', protected_view, name='protected_view'),

    path('save/', save, name='save'),
    path('get/<str:key>/', get, name='get'),
    path('delete/<str:key>/', delete, name='delete'),
]
