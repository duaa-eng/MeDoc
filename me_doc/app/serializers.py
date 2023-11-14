# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Patient, Doctor
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["user", "name", "email", "contact","timestamp"]
        
class DoctorSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Doctor
        fields = ["user","name" , "email", "contact", "speciality","timestamp"]