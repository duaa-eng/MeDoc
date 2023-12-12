from django.shortcuts import render, redirect  
from web_app.forms import PatientForm  
from web_app.models import Patient, Doctor , PatientAppointment, DoctorAppointment
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import DoctorSerializer, PatientSerializer, PatientAppointmentSerializer, DoctorAppointmentSerializer

class PatientApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        todos = Patient.objects.filter(user = request.user.id)
        serializer = PatientSerializer(Patient, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    # 2. Create
    def post(self, request, *args, **kwargs):
        
        data = {
            'name': request.data.get('name'), 
            'email': request.data.get('email'), 
            'contact': request.data.get('contact'),
            'user': request.user.id
        }
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        
        todos = Doctor.objects.filter(user = request.user.id)
        serializer = DoctorSerializer(Doctor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    # 2. Create
    def post(self, request, *args, **kwargs):
        
        data = {
            'name': request.data.get('name'), 
            'email': request.data.get('email'), 
            'contact': request.data.get('contact'),
            'speciality': request.data.get('speciality'),
            'user': request.user.id
        }
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientAppointmentApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # List all appointments for a patient
    def get(self, request, *args, **kwargs):
        appointments = PatientAppointment.objects.filter(patient__user=request.user)
        serializer = PatientAppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Register a new appointment
    def post(self, request, *args, **kwargs):
        serializer = PatientAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorAppointmentApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # List all appointments for a doctor
    def get(self, request, *args, **kwargs):
        appointments = DoctorAppointment.objects.filter(doctor__user=request.user)
        serializer = DoctorAppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Example: Cancel an appointment
    # You'll need to define the logic for identifying the specific appointment to cancel
    def delete(self, request, appointment_id, *args, **kwargs):
        try:
            appointment = DoctorAppointment.objects.get(id=appointment_id, doctor__user=request.user)
            appointment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except DoctorAppointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
