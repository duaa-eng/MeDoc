# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import DoctorAppointment, Patient, Doctor, PatientAppointment



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["user", "name", "email", "contact","timestamp"]
        
class DoctorSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Doctor
        fields = ["user","name" , "email", "contact", "speciality","timestamp"]

class PatientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientAppointment
        fields=["patient","doctor","appointment_time","status","notes"]

        
class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorAppointment
        fiels=["doctor","patient","appointment_time","status","notes"]

        