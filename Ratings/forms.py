from django import forms
from django.contrib.auth import get_user_model
from Ratings.models import Rating
from django.contrib.auth import authenticate

# User = get_user_model()


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['character_and_conduct', 'professional_skill', 'patient_centered_care']
        