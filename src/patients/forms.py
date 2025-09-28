from django.forms import ModelForm, TextInput, Textarea, Select, DateInput, NumberInput

from .models import Patient, PatientConsultations


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'gender': 'Género',
            'address': 'Dirección',
            'occupation': 'Ocupación',
            'phone': 'Teléfono',
            'birthday': 'Fecha de nacimiento',
            'DocumentID': 'Documento',
            'familyHistory': 'Antecedentes familiares',
            'created_at': 'Creado el',
            'updated_at': 'Actualizado el',
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'lastname': TextInput(attrs={'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'address': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'occupation': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'birthday': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'DocumentID': TextInput(attrs={'class': 'form-control', 'maxlength': '8', 'inputmode': 'numeric', 'pattern': '\\d{8}', 'placeholder': '8 dígitos'}),
            'familyHistory': Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean_DocumentID(self):
        value = self.cleaned_data.get('DocumentID', '')
        if value is None:
            value = ''
        value = str(value).strip()
        if len(value) != 8:
            from django.core.exceptions import ValidationError
            raise ValidationError('El documento debe tener exactamente 8 dígitos.')
        if not value.isdigit():
            from django.core.exceptions import ValidationError
            raise ValidationError('El documento solo puede contener números (0-9).')
        return value


class PatientConsultationForm(ModelForm):
    class Meta:
        model = PatientConsultations
        exclude = ['patient']
        labels = {
            'symptoms': 'Síntomas',
            'date': 'Fecha',
            'diagnosis': 'Diagnóstico',
            'notes': 'Notas',
            'chiefComplaint': 'Motivo principal',
        }
        widgets = {
            'symptoms': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'diagnosis': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'notes': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'chiefComplaint': Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }