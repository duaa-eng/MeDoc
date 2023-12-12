from django import forms  
from web_app.models import Patient  
class PatientForm(forms.ModelForm):  
    class Meta:  
        model = Patient
        fields = "__all__"  