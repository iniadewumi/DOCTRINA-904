from django.shortcuts import render
from .models import HospitalSystem
from Doctors.models import Doctor
# Create your views here.

def HospitalPage(request, hospital_npi_id):
    print(request.GET)
    hospital = HospitalSystem.objects.get(pk=hospital_npi_id)
    doctors = Doctor.objects.filter(hospital_system=hospital_npi_id)
    context = {
        'hospital': hospital,
        'doctors': doctors
        }
    return render(request, 'Pages/Hospital.html', context=context)
