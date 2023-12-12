from django.db import models  
from django.contrib.auth.models import User


class Patient(models.Model):  
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)  
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    class Meta:  
        db_table = "patient" 
    def __str__(self):
        return self.name 

class Doctor(models.Model):  
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)  
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField() 
    speciality= models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    class Meta:  
        db_table = "doctor" 
    def __str__(self):
        return self.name 

class PatientAppointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=100, default='Scheduled')  # e.g., Scheduled, Completed, Cancelled
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "patient_appointment"

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} on {self.appointment_time}"

class DoctorAppointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=100, default='Scheduled')  # e.g., Scheduled, Completed, Cancelled
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "doctor_appointment"

    def __str__(self):
        return f"{self.doctor.name} with {self.patient.name} on {self.appointment_time}"

        