from django.db import models
from django.utils import timezone
from datetime import time

# Enum choices
class Status(models.TextChoices):
    APPROVED = 'APPROVED', 'Approved'
    PENDING = 'PENDING', 'Pending'
    REJECTED = 'REJECTED', 'Rejected'

class ERole(models.TextChoices):
    PATIENT = 'PATIENT', 'Patient'
    DOCTOR = 'DOCTOR', 'Doctor'
    ADMIN = 'ADMIN', 'Admin'

class ScheduleState:
    WAITING = 0
    ACCEPTED = 1
    CANCELED = 2
    DONE = 3
    MISSED = 4
    REJECTED = 5

    STATE_CHOICES = [
        (WAITING, 'Chờ xác nhận'),
        (ACCEPTED, 'Đã xác nhận'),
        (CANCELED, 'Đã hủy'),
        (DONE, 'Đã hoàn thành'),
        (MISSED, 'Đã bỏ lỡ'),
        (REJECTED, 'Đã từ chối'),
    ]


# Models
class Department(models.Model):
    name = models.TextField()
    description = models.TextField()
    location = models.TextField()

class UserModel(models.Model):
    fullname = models.CharField(max_length=255)
    gender = models.BooleanField()
    birthday = models.DateField()
    telephone = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ERole.choices)

class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=Status.choices)
    author = models.ForeignKey(UserModel, related_name="articles", on_delete=models.CASCADE)

class Doctor(models.Model):
    position = models.CharField(max_length=255)
    description = models.TextField()
    room_address = models.CharField(max_length=255)
    service_prices = models.IntegerField()
    department = models.ForeignKey(Department, related_name="doctors", on_delete=models.CASCADE)
    user = models.OneToOneField(UserModel, related_name="doctor_profile", on_delete=models.CASCADE)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(UserModel, related_name="patient_profile", on_delete=models.CASCADE)
    nhommau = models.CharField(max_length=10)
    cannang = models.FloatField()
    chieucao = models.FloatField()
    benhnen = models.TextField()

class Shift(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()

class Schedule(models.Model):
    date = models.DateField()
    state = models.IntegerField(choices=ScheduleState.STATE_CHOICES, default=ScheduleState.WAITING)
    doctor = models.ForeignKey(Doctor, related_name="schedules", on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name="schedules", on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, related_name="schedules", on_delete=models.CASCADE)

class MedicalRecord(models.Model):
    schedule = models.OneToOneField(Schedule, related_name="medical_record", on_delete=models.CASCADE)
    diagnosis = models.TextField()

class Role(models.Model):
    name = models.CharField(max_length=20, choices=ERole.choices)
    users = models.ManyToManyField(UserModel, related_name="roles")
