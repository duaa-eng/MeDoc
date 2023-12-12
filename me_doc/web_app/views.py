from django.shortcuts import render, redirect  
from web_app.forms import PatientForm  
from web_app.models import Patient, Doctor , PatientAppointment, DoctorAppointment
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import DoctorSerializer, PatientSerializer, PatientAppointmentSerializer, DoctorAppointmentSerializer

class PatientAPIView(APIView):
    # Get all patients or create a new one
    def get(self, request, format=None):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetailAPIView(APIView):
    # Retrieve, update or delete a patient instance
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorAPIView(APIView):
    # Get all doctors or create a new one
    def get(self, request, format=None):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetailAPIView(APIView):
    # Retrieve, update or delete a doctor instance
    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        doctor = self.get_object(pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientAppointmentAPIView(APIView):
    # Get all patient appointments or create a new one
    def get(self, request, format=None):
        appointments = PatientAppointment.objects.all()
        serializer = PatientAppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientAppointmentDetailAPIView(APIView):
    # Retrieve, update or delete a patient appointment instance.
    def get_object(self, pk):
        try:
            return PatientAppointment.objects.get(pk=pk)
        except PatientAppointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = PatientAppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = PatientAppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DoctorAppointmentAPIView(APIView):
    # Get all doctor appointments or create a new one
    def get(self, request, format=None):
        appointments = DoctorAppointment.objects.all()
        serializer = DoctorAppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorAppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorAppointmentDetailAPIView(APIView):
    # Retrieve, update or delete a doctor appointment instance.
    def get_object(self, pk):
        try:
            return DoctorAppointment.objects.get(pk=pk)
        except DoctorAppointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = DoctorAppointmentSerializer(appointment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appointment = self.get_object(pk)
        serializer = DoctorAppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        appointment = self.get_object(pk)
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

