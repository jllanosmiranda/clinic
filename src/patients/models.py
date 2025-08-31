from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class History(models.Model):
    Gender = (
        (True, 'Masculino'),
        (False, 'Femenino'),
    )
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    gender = models.BooleanField(choices=Gender)
    address = models.TextField()
    occupation = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


