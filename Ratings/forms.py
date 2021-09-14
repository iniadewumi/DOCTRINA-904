from django import forms
from django.contrib.auth import get_user_model
from Ratings.models import Rating
from django.contrib.auth import authenticate

# User = get_user_model()


class QuestionnaireForm(forms.Form):
    doctor = forms.IntegerField(required=False, widget=forms.HiddenInput())

    collab = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    accepts_responsibility = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    like_doc = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    

    appropriate_diagnosis = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    high_stress_effectiveness = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    communication_to_staff = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    mindful_prescription = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    trust_for_personal_care = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))


    recommend_regardless_of_personality = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    ethical_practices = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    quality_care = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    improve_care = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect(attrs={'class':'checkbox'}))
    why_improve_care = forms.CharField(max_length=200, widget=forms.Textarea)
    good_patient_outcome = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    
    recog_psychosocial = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))   
    
    genuine_patient_care  = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    # emotional_intelligence = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    effective_patient_communication = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    empathy  = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    legal_awareness  = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    patient_relationship  = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    room_for_improvement = forms.CharField(max_length=200, widget=forms.Textarea)

    anonymous_comment = forms.CharField(max_length=200, widget=forms.Textarea)
    whistle_blow = forms.BooleanField(widget=forms. CheckboxInput(attrs={'id':'whistle_blow', 'class': 'checkbox'}), required=False)
    whistleblow_text = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': "Enter your input here. All information is anonymous and will not be linked to you as a user in any way."}), required=False)
