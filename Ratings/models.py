from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey('Doctors.Doctor', on_delete=models.CASCADE)

class CharacterConductRatings(models.Model):
    rating_obj = models.OneToOneField(Rating, on_delete=models.CASCADE)
    collab = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    accepts_responsibilities = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    like_doc = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    
class ProfessionalSkill(models.Model):
    rating_obj = models.OneToOneField(Rating, on_delete=models.CASCADE)
    appropriate_diagnosis = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    high_stress_effectiveness = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    communication_to_staff = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    mindful_prescription = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    trust_for_personal_care = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])


    recommend_regarless_of_personality = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    ethical_practices = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    quality_care = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    improve_care = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    why_improve_care = models.TextField(null=True, blank=True)
    good_patient_outcome = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    

class PatientCare(models.Model):
    rating_obj = models.OneToOneField(Rating, on_delete=models.CASCADE)
    recog_psychosocial = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    effective_patient_communication  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    empathy = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    legal_awareness  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    patient_relationship  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    genuine_patient_care  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])


class Anonymous_Comment_and_Whistelblow(models.Model):    
    rating_obj = models.OneToOneField(Rating, on_delete=models.CASCADE)
    anonymous_comment = models.TextField(null=True)
    whistelblow = models.BooleanField(default=False, blank=True)
    whistleblow_text = models.TextField(null=True, blank=True)

# class GeneralTenants(models.Model):
#     rating = models.OneToOneField('Rating', on_delete=models.CASCADE)
#     emotional_intelligence = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
#     effective_patient_communication = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
#     empathy  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
#     legal_awareness  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
#     patient_relationship  = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    
@receiver(post_save, sender=Rating)
def create_or_update(sender, instance, created, **kwargs):
    if created:
        instance.acw = Anonymous_Comment_and_Whistelblow.objects.create(rating_obj=instance)
        instance.pc = PatientCare.objects.create(rating_obj=instance)
        instance.ps = ProfessionalSkill.objects.create(rating_obj=instance)
        instance.ccr = CharacterConductRatings.objects.create(rating_obj=instance)
        