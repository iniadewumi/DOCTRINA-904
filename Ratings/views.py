
from django.shortcuts import render
from Doctors.models import Doctor
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/signup")
def RateDoctor(request, doctor_npi_id):
    doctor = Doctor.objects.get(pk=doctor_npi_id)
    context = {'doctor': doctor}
    return render(request, 'Ratings/Rate-Doctor.html', context=context)

@login_required(login_url="/signup")
def ThankYou(request, doctor_npi_id):
    form = request.POST
    print(form)
    doctor = Doctor.objects.get(pk = doctor_npi_id)
    return render(request, 'Ratings/ThankYou.html', context={'doctor': doctor})
