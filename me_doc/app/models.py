from django.db import models  
from django.contrib.auth.models import User

class Patient(models.Model):  
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15)  
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    class Meta:  
        db_table = "patient" 
    def __str__(self):
        return self.name 

class Doctor(models.Model):  
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15)  
    speciality= models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    class Meta:  
        db_table = "doctor" 
    def __str__(self):
        return self.name 