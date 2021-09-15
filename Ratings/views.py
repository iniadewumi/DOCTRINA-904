
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
    doctor_obj = Doctor.objects.get(pk=doctor_npi_id)

    form = QuestionnaireForm()
    form.fields['doctor'].initial = doctor_obj
    
    if request.method == 'POST':

        form = QuestionnaireForm(request.POST)
    
        if form.is_valid():
            form.cleaned_data['doctor'] = doctor_obj
            form.save()
            print("\n\n\n", user)
            return HttpResponseRedirect(f'/{doctor_npi_id}/thank_you')
        else:
            print(dir(form))
            print(form.non_field_errors)
            print(form.errors)
            
            form = QuestionnaireForm()

    context = {'doctor': doctor_obj, 'form': form, 'user':user}
    return render(request, 'Ratings/Rate-Doctor.html', context=context)


@login_required(login_url="/login")
def ThankYou(request, doctor_npi_id):
    form = request.POST
    print(form)
    doctor = Doctor.objects.get(pk = doctor_npi_id)
    
    return render(request, 'Ratings/ThankYou.html', context={'doctor': doctor_obj})
