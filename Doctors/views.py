from django.shortcuts import render
from .models import Doctor
from Ratings.models import Rating
# Create your views here.
from django.db.models import Avg


def DoctorPage(request, doctor_npi_id):
    doctor = Doctor.objects.get(pk=doctor_npi_id)

    ratings = Rating.objects.filter(doctor_id=doctor_npi_id)

    try:
        doc_total_average = round(sum(x.total_average for x in ratings)/len(ratings), 2)
    except:
        doc_total_average = sum(x.total_average for x in ratings)
    
    ltenants = [[x.patient_centered_care, x.professional_skill, x.character_and_conduct] for x in ratings]

    tenants  = [(sum(i)*100/(5*len(ratings))) for i in zip(*ltenants)]

    context = {'doctor': doctor, 'ratings':ratings, 'doc_total_average':doc_total_average, "tenants":tenants}
    return render(request, 'Pages/Doctor-Page.html', context=context)

    # a = {i:v for (i, v)  in nums if type(v)==int}
    # # a = [x for x in ratings ]