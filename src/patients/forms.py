from django.forms import ModelForm

from patients.models import History


class PatientForm(ModelForm):
    class Meta:
        model = History
        fields = '__all__'