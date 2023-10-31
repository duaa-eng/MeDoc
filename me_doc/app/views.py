from django.shortcuts import render, redirect  
from app.forms import PatientForm  
from app.models import Patient  
# Create your views here.  
def patient(request):  
    if request.method == "POST":  
        form = PatientForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = PatientForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    patients = Patient.objects.all()  
    return render(request,"show.html",{'patients':patients})  
def edit(request, id):  
    patients = Patient.objects.get(id=id)  
    return render(request,'edit.html', {'patients':patients})  
def update(request, id):  
    patients = Patient.objects.get(id=id)  
    form = PatientForm(request.POST, instance = patients)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'patients': patients})  
def destroy(request, id):  
    patients = Patient.objects.get(id=id)  
    patients.delete()  
    return redirect("/show")  