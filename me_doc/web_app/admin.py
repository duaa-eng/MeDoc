from django.contrib import admin
from .models import DoctorAppointment, Patient, Doctor, PatientAppointment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PatientAppointment)
admin.site.register(DoctorAppointment)
# Register your models here.
