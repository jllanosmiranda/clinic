from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, PatientConsultationForm
from .models import Patient, PatientConsultations, TreatmentPlan, TriageRecords
import logging
from .filters import PatientFilter, ConsultationFilter, AllConsultationsFilter

log = logging.getLogger(__name__)


def new_history(request):
    # Create a new Patient
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return redirect('history_detail', history_id=patient.id)
    else:
        form = PatientForm()

    context = {'form': form}
    return render(request, template_name='patients/historyNew.html', context=context)


def history_list(request):
    # List and filter Patients
    qs = Patient.objects.all()
    patient_filter = PatientFilter(request.GET, queryset=qs)
    context = {
        'filter': patient_filter,
        'objects': patient_filter.qs,
    }
    return render(request, template_name='patients/historyList.html', context=context)


def history_detail(request, history_id):
    # Patient detail with filtered consultations table
    patient = get_object_or_404(Patient, id=history_id)
    consultations_qs = PatientConsultations.objects.filter(patient=patient).order_by('-date')
    consultation_filter = ConsultationFilter(request.GET, queryset=consultations_qs)
    context = {
        'object': patient,
        'consultation_filter': consultation_filter,
        'consultations': consultation_filter.qs,
    }
    return render(request, template_name='patients/historyDetail.html', context=context)


def consultation_detail(request, consultation_id):
    # Consultation detail: list treatments and triage records
    consultation = get_object_or_404(PatientConsultations, id=consultation_id)
    treatments = TreatmentPlan.objects.filter(consultation=consultation)
    triages = TriageRecords.objects.filter(consultation=consultation)
    context = {
        'consultation': consultation,
        'treatments': treatments,
        'triages': triages,
    }
    return render(request, template_name='patients/consultationDetail.html', context=context)


def consultations_list(request):
    # Global list of consultations with filters by patient document and date range
    qs = PatientConsultations.objects.select_related('patient').all().order_by('-date')
    filt = AllConsultationsFilter(request.GET, queryset=qs)
    context = {
        'filter': filt,
        'consultations': filt.qs,
    }
    return render(request, template_name='patients/consultationsList.html', context=context)


def new_consultation(request, history_id):
    # Create a new consultation for a patient
    patient = get_object_or_404(Patient, id=history_id)
    if request.method == 'POST':
        form = PatientConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = patient
            consultation.save()
            return redirect('consultation_detail', consultation_id=consultation.id)
    else:
        form = PatientConsultationForm()

    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, template_name='patients/consultationNew.html', context=context)
