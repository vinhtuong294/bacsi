from django.db import models

class ERole(models.TextChoices):
    PATIENT = 'PATIENT', 'Patient'
    DOCTOR = 'DOCTOR', 'Doctor'
    ADMIN = 'ADMIN', 'Admin'
# Create your models here.

class UserModel(models.Model):
    fullname = models.CharField(max_length=255)
    gender = models.BooleanField()
    birthday = models.DateField()
    telephone = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ERole.choices)