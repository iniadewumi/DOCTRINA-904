from django import forms
from django.contrib.auth import get_user_model
from Ratings.models import Rating
from Nurses.models import Profile
from django.contrib.auth import authenticate

# User = get_user_model()


class QuestionnaireForm(forms.ModelForm):

    collab = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    accepts_responsibility = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    like_doc = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    

    appropriate_diagnosis = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    high_stress_effectiveness = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    communication_to_staff = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    mindful_prescription = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    trust_for_personal_care = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))


    recommend_regardless_of_personality = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect(attrs={'class':'checkbox'}))
    ethical_practices = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    quality_care = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    improve_care = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect(attrs={'class':'checkbox'}))
    why_improve_care = forms.CharField(max_length=200, widget=forms.Textarea, required=False)
    good_patient_outcome = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    
    recog_psychosocial = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))   
    
    genuine_patient_care  = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    # emotional_intelligence = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    effective_patient_communication = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    empathy  = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    legal_awareness  = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    patient_relationship  = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'max':'100', 'min':'0'}))
    # room_for_improvement = forms.CharField(max_length=200, widget=forms.Textarea)

    anonymous_comment = forms.CharField(max_length=200, widget=forms.Textarea)
    whistle_blow = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'whistle_blow', 'class': 'checkbox'}), required=False)
    whistleblow_text = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': "Enter your input here. All information is anonymous and will not be linked to you as a user in any way."}), required=False)

    class Meta:
        model = Rating
        fields = ['doctor_obj', 'recog_psychosocial', 'effective_patient_communication', 'empathy' 
        ,'legal_awareness', 'patient_relationship', 'genuine_patient_care' 
        ,'appropriate_diagnosis', 'high_stress_effectiveness'
        , 'communication_to_staff', 'mindful_prescription',  'trust_for_personal_care', 'ethical_practices' 
        ,'quality_care', 'improve_care', 'why_improve_care', 'good_patient_outcome', 
        'collab', 'accepts_responsibility', 'like_doc', 'anonymous_comment', 'whistleblow_text']
        # exclude = ['doctor_obj']
        # fields = "__all__"


        # fields = ['doctor_obj', 'recog_psychosocial', 'effective_patient_communication', 'empathy' 
        # ,'legal_awareness', 'patient_relationship', 'genuine_patient_care' 
        # ,'appropriate_diagnosis', 'high_stress_effectiveness'
        # , 'communication_to_staff', 'mindful_prescription',  'trust_for_personal_care', 'ethical_practices' 
        # ,'quality_care', 'improve_care', 'why_improve_care', 'good_patient_outcome', 
        # 'collab', 'accepts_responsibility', 'like_doc', 'anonymous_comment', 'whistleblow_text']
    # def clean(self, *args, **kwargs):
    #     doctor_obj =self.cleaned_data['doctor_obj']
    #     recog_psychosocial = self.cleaned_data['recog_psychosocial']
    #     effective_patient_communication = self.cleaned_data['effective_patient_communication']
    #     empathy = self.cleaned_data['empathy']
    #     legal_awareness = self.cleaned_data['legal_awareness']
    #     patient_relationship = self.cleaned_data['patient_relationship']
    #     genuine_patient_care = self.cleaned_data['genuine_patient_care'], 
    #     appropriate_diagnosis = self.cleaned_data['appropriate_diagnosis']
    #     high_stress_effectiveness = self.cleaned_data['high_stress_effectiveness']
    #     communication_to_staff = self.cleaned_data['communication_to_staff']
    #     mindful_prescription = self.cleaned_data['mindful_prescription'], 
    #     trust_for_personal_care = self.cleaned_data['trust_for_personal_care']
    #     ethical_practices = self.cleaned_data['ethical_practices']
    #     quality_care=self.cleaned_data['quality_care']
    #     improve_care =self.cleaned_data['improve_care']
    #     why_improve_care =self.cleaned_data['why_improve_care']
    #     good_patient_outcome = self.cleaned_data['good_patient_outcome']
        
    #     collab = self.cleaned_data['collab']
    #     accepts_responsibility =  self.cleaned_data['accepts_responsibility']
    #     like_doc = self.cleaned_data['like_doc']
    #     anonymous_comment=self.cleaned_data['anonymous_comment']
    #     whistleblow_text = self.cleaned_data['whistleblow_text']

    #     return super(QuestionnaireForm, self).clean(*args, **kwargs)
    # def save(self, commit=True):
    #     questionnaire = super().save(commit=False)
    #     if commit:
    #         questionnaire.save()
    #     return questionnaire


    # def save(self):
    #     data = self.cleaned_data
    #     # profile = Profile(user=self.user, work_experience= data['experience-years'], job_title= data['job_title'], other_positions=['other-experience'], department=data['department'])
    #     # print(profile)
    #     # profile.save()

    #     # rating = Rating.objects.create()

    #     print(rating)
    #     rating.save()
    #     return rating

