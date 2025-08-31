
from django.urls import path
from .views import new_history, history_list, history_detail

urlpatterns = [
    path('history/', new_history, name='new_history'),
    path('history/list/', history_list, name='history_list'),
    path('history/<int:history_id>/details', history_detail, name='history_detail'),
]
