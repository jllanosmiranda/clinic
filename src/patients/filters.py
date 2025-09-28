import django_filters
from django import forms
from django_filters.widgets import RangeWidget
from .models import Patient, PatientConsultations


class PatientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Nombre')
    lastname = django_filters.CharFilter(field_name='lastname', lookup_expr='icontains', label='Apellido')
    DocumentID = django_filters.CharFilter(
        field_name='DocumentID',
        lookup_expr='exact',
        label='Documento',
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '8', 'inputmode': 'numeric', 'pattern': '\\d{8}'})
    )

    class Meta:
        model = Patient
        fields = ['name', 'lastname', 'DocumentID']


class ConsultationFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(
        field_name='date',
        label='Rango de fechas',
        widget=RangeWidget(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = PatientConsultations
        fields = ['date']


class AllConsultationsFilter(django_filters.FilterSet):
    document = django_filters.CharFilter(
        field_name='patient__DocumentID',
        label='Documento',
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '8', 'inputmode': 'numeric', 'pattern': '\\d{8}'})
    )
    date = django_filters.DateFromToRangeFilter(
        field_name='date',
        label='Rango de fechas',
        widget=RangeWidget(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = PatientConsultations
        fields = ['document', 'date']
