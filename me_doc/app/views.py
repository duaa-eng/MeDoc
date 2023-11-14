from django.shortcuts import render, redirect  
from app.forms import PatientForm  
from app.models import Patient, Doctor  
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import DoctorSerializer, PatientSerializer

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