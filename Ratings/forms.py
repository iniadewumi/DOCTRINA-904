from django import forms
from django.contrib.auth import get_user_model
from Ratings.models import Rating
from Nurses.models import Profile
from django.contrib.auth import authenticate

# User = get_user_model()


class QuestionnaireForm(forms.ModelForm):
    CHOICES = [ 
        (1, '1'),
        (2, '2'), 
        (3, '3'), 
        (4, '4'), 
        (5, '5')
    ]
    collab = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    accepts_responsibility = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    like_doc = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    

    appropriate_diagnosis = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    high_stress_effectiveness = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    communication_to_staff = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    mindful_prescription = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    trust_for_personal_care = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


    recommend_regardless_of_personality = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect(attrs={'class':'checkbox'}))
    ethical_practices = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    quality_care = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    improve_care = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')], widget=forms.RadioSelect(attrs={'class':'checkbox'}))
    why_improve_care = forms.CharField(max_length=200, widget=forms.Textarea, required=False)
    good_patient_outcome = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    

    recog_psychosocial = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    
    genuine_patient_care  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    # emotional_intelligence = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    effective_patient_communication = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    empathy  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    legal_awareness  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    patient_relationship  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    # room_for_improvement = forms.CharField(max_length=200, widget=forms.Textarea)

    anonymous_comment = forms.CharField(max_length=200, widget=forms.Textarea)
    whistle_blow = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'whistle_blow', 'class': 'checkbox'}), required=False)
    whistleblow_text = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': "Enter your input here. All information is anonymous and will not be linked to you as a user in any way."}), required=False)

    class Meta:
        model = Rating
        fields = ['doctor', 'recog_psychosocial', 'effective_patient_communication', 'empathy' 
        ,'legal_awareness', 'patient_relationship', 'genuine_patient_care' 
        ,'appropriate_diagnosis', 'high_stress_effectiveness'
        , 'communication_to_staff', 'mindful_prescription',  'trust_for_personal_care', 'ethical_practices' 
        ,'quality_care', 'improve_care', 'why_improve_care', 'good_patient_outcome', 
        'collab', 'accepts_responsibility', 'like_doc', 'anonymous_comment', 'whistleblow_text']
        # exclude = ['doctor']
        # fields = "__all__"


        # fields = ['doctor', 'recog_psychosocial', 'effective_patient_communication', 'empathy' 
        # ,'legal_awareness', 'patient_relationship', 'genuine_patient_care' 
        # ,'appropriate_diagnosis', 'high_stress_effectiveness'
        # , 'communication_to_staff', 'mindful_prescription',  'trust_for_personal_care', 'ethical_practices' 
        # ,'quality_care', 'improve_care', 'why_improve_care', 'good_patient_outcome', 
        # 'collab', 'accepts_responsibility', 'like_doc', 'anonymous_comment', 'whistleblow_text']
    # def clean(self, *args, **kwargs):
    #     doctor =self.cleaned_data['doctor']
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

