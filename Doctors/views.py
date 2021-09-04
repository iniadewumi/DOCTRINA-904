from django.shortcuts import render
from .models import Doctor
# Create your views here.

def DoctorPage(request, doctor_npi_id):
    doctor = Doctor.objects.get(pk=doctor_npi_id)
    context = {'doctor': doctor}
    return render(request, 'Pages/Doctor-Page.html', context=context)

