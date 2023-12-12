from django import forms  
from web_app.models import Patient, Doctor, DoctorAppointment, PatientAppointment
class PatientForm(forms.ModelForm):  
    class Meta:  
        model = Patient
        fields = "__all__"  

class DoctorForm(forms.ModelForm):  
    class Meta:  
        model = Doctor
        fields = "__all__"  

class PatientAppointmentForm(forms.ModelForm):  
    class Meta:  
        model = PatientAppointment
        fields = "__all__"  

class DoctorAppointmentForm(forms.ModelForm):  
    class Meta:  
        model = DoctorAppointment
        fields = "__all__"  