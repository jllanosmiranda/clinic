from django.urls import path
from .views import new_history, history_list, history_detail, consultation_detail, consultations_list, new_consultation

urlpatterns = [
    path('history/', new_history, name='new_history'),  # create patient
    path('history/list/', history_list, name='history_list'),  # list/filter patients
    path('history/<int:history_id>/details', history_detail, name='history_detail'),  # patient detail with consultations
    path('history/<int:history_id>/consultation/new', new_consultation, name='consultation_new'),  # create consultation
    path('consultation/<int:consultation_id>/details', consultation_detail, name='consultation_detail'),  # consultation detail
    path('consultations/', consultations_list, name='consultations_list'),  # all consultations list
]
