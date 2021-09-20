
from django.shortcuts import render
from Doctors.models import Doctor
from Nurses.models import User
from Ratings.models import Rating
from .forms import QuestionnaireForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponseRedirect

@login_required(login_url="/login")
def RateDoctor(request, doctor_npi_id):
    user = User.objects.filter(email=request.user)[0]
    doctor = Doctor.objects.get(pk=doctor_npi_id)
    ratings = Rating.objects.filter(doctor_id=doctor_npi_id)
    try:
        doc_total_average = round(sum(x.total_average for x in ratings)/len(ratings), 2)
    except:
        doc_total_average = sum(x.total_average for x in ratings)
    
    ltenants = [[int(x.patient_centered_care), round(x.professional_skill), int(x.character_and_conduct)] for x in ratings]

    tenants  = [(sum(i)*100/(5*len(ratings))) for i in zip(*ltenants)]


    form = QuestionnaireForm()
    form.fields['doctor'].initial = doctor
    
    if request.method == 'POST':

        form = QuestionnaireForm(request.POST)
    
        if form.is_valid():
            form.cleaned_data['doctor'] = doctor
            form.save()
            print("\n\n\n", user)
            return HttpResponseRedirect(f'/{doctor_npi_id}/thank_you')
        else:
            print(dir(form))
            print(form.non_field_errors)
            print(form.errors)
            
            form = QuestionnaireForm()

    context = {'doctor': doctor, 'form': form, 'user':user, 'ratings': ratings, "tenants":tenants, 'doc_total_average':doc_total_average}
    return render(request, 'Ratings/Rate-Doctor.html', context=context)


@login_required(login_url="/login")
def ThankYou(request, doctor_npi_id):
    form = request.POST

    doctor = Doctor.objects.get(pk = doctor_npi_id)
    
    return render(request, 'Ratings/ThankYou.html', context={'doctor': doctor})
