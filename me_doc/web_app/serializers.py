# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import DoctorAppointment, Patient, Doctor, PatientAppointment



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'email', 'contact_number', 'date_of_birth', 'address','timestamp']
        
class DoctorSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'contact_number', 'address','speciality','timestamp']

class PatientAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PatientAppointment
        fields = '__all__' 

        
class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=DoctorAppointment
        fields = '__all__' 

        