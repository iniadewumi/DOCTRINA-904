from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey('Doctors.Doctor', on_delete=models.CASCADE)
    character_and_conduct = models.OneToOneField('CharacterConductRatings', on_delete=models.CASCADE)
    professional_skill = models.OneToOneField('ProfessionalSkill', on_delete=models.CASCADE)
    patient_centered_care = models.OneToOneField('PatientCare', on_delete=models.CASCADE)
    anonymous_comment = models.OneToOneField('Anonymous_Comment_and_Whistelblow', on_delete=models.CASCADE)

    total_average = models.FloatField()

class CharacterConductRatings(models.Model):
    collab = models.BooleanField(default=False)
    accepts_responsibilities = models.BooleanField(default=False)
    like_doc = models.BooleanField(default=False)
    
class ProfessionalSkill(models.Model):
    appropriate_diagnosis = models.BooleanField(default=False)
    high_stress_effectiveness = models.BooleanField(default=False)
    communication_to_staff = models.BooleanField(default=False)
    mindful_prescription = models.BooleanField(default=False)
    trust_for_personal_care = models.BooleanField(default=False)


    recommend_regarless_of_personality = models.BooleanField(default=False)
    ethical_practices = models.BooleanField(default=False)
    quality_care = models.BooleanField(default=False)
    improve_care = models.BooleanField(default=False)
    why_improve_care = models.TextField(null=True, blank=True)
    good_patient_outcome = models.BooleanField(default=False)
    
    

class PatientCare(models.Model):
    recog_psychosocial = models.BooleanField(default=False)
    communicates_effectively_patients  = models.BooleanField(default=False)
    empathy_to_patient_fam = models.BooleanField(default=False)
    aware_of_rights  = models.BooleanField(default=False)
    good_patient_rel  = models.BooleanField(default=False)
    genuine_patient_care  = models.BooleanField(default=False)

class GeneralTenants(models.Model):
    emotional_intelligence = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    effective_patient_communication = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    empathy  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    legal_awareness  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    patient_relationship  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    room_for_improvement = models.TextField()

class Anonymous_Comment_and_Whistelblow(models.Model):    
    anonymous_comment = models.TextField(null=True)
    whistelblow = models.BooleanField(default=False, blank=True)
    whistleblow_text = models.TextField(null=True, blank=True)
