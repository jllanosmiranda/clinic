
from django.urls import path
from .views import new_history

urlpatterns = [
    path('history/', new_history, name='new_history'),
]
