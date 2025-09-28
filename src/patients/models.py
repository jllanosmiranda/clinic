from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Patient(models.Model):
    Gender = (
        (True, 'Masculino'),
        (False, 'Femenino'),
    )
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.BooleanField(choices=Gender)
    address = models.TextField()
    occupation = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    birthday = models.DateField()
    DocumentID = models.CharField(max_length=8)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    familyHistory = models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']

class TriageRecords(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    heartRate = models.IntegerField()
    systolicPressure = models.IntegerField()
    diastolicPressure = models.IntegerField()
    oxygenSaturation = models.DecimalField(max_digits=3, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    respiratoryRate = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=3, decimal_places=2)
    height = models.IntegerField()
    Notes = models.TextField()

class  PatientConsultations(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    triage = models.ForeignKey(TriageRecords, on_delete=models.CASCADE, default=0)
    symptoms = models.TextField()
    date = models.DateField()
    diagnosis = models.TextField()
    notes = models.TextField()
    chiefComplaint = models.TextField()

class TreatmentPlan(models.Model):
    consultation = models.ForeignKey(PatientConsultations, on_delete=models.CASCADE)
    treatment = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Tests(models.Model):
    consultation = models.ForeignKey(PatientConsultations, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    testResult = models.TextField()







