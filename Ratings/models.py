from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey('Doctors.Doctor', on_delete=models.CASCADE)

# class CharacterConductRatings(models.Model):
    # rating_obj = models.OneToOneField(Rating, on_delete=models.CASCADE)
    collab = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    accepts_responsibility = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    like_doc = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    
# class ProfessionalSkill(models.Model):
    # rating_obj = models.OneToOneField(Rating, on_delete=models.CASCADE)
    appropriate_diagnosis = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    high_stress_effectiveness = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    communication_to_staff = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    mindful_prescription = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    trust_for_personal_care = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])


    recommend_regarless_of_personality = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    ethical_practices = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    quality_care = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    improve_care = models.BooleanField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    why_improve_care = models.TextField(null=True, blank=True)
    good_patient_outcome = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    

# class PatientCare(models.Model):
    # rating_obj = models.OneToOneField(Rating, on_delete=models.CASCADE)
    recog_psychosocial = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    effective_patient_communication  = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    empathy = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    legal_awareness  = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    patient_relationship  = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    genuine_patient_care  = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])


# class Anonymous_Comment_and_Whistelblow(models.Model):    
    # rating_obj = models.OneToOneField(Rating, on_delete=models.CASCADE)
    anonymous_comment = models.TextField(null=True)
    whistelblow = models.BooleanField(default=False, blank=True)
    whistleblow_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return " ".join([self.doctor.first_name , self.doctor.last_name,  str(self.rating_id)])

    @property
    def patient_centered_care(self):
        pcc = [self.recog_psychosocial, self.effective_patient_communication, self.empathy, self.legal_awareness, self.patient_relationship, self.genuine_patient_care]
        return sum(pcc)/len(pcc)
    @property
    def professional_skill(self):
        ps = [self.ethical_practices , self.quality_care , self.good_patient_outcome , self.appropriate_diagnosis , self.high_stress_effectiveness , self.communication_to_staff , self.mindful_prescription]
        return sum(ps)/len(ps)
    @property
    def character_and_conduct(self):
        cac = [self.like_doc, self.accepts_responsibility, self.collab]
        return sum(cac)/len(cac)
    @property
    def total_average(self):
        _Sum = self.professional_skill + self.character_and_conduct +self.patient_centered_care
        return (_Sum/3)
        
    @property
    def doc_name(self):
        return ", ".join([self.doctor.last_name, self.doctor.first_name])

# class GeneralTenants(models.Model):
#     rating = models.OneToOneField('Rating', on_delete=models.CASCADE)
#     emotional_intelligence = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
#     effective_patient_communication = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
#     empathy  = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
#     legal_awareness  = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
#     patient_relationship  = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    
# @receiver(post_save, sender=Rating)
# def create_or_update(sender, instance, created, **kwargs):
#     if created:
#         instance.acw = Anonymous_Comment_and_Whistelblow.objects.create(rating_obj=instance)
#         instance.pc = PatientCare.objects.create(rating_obj=instance)
#         instance.ps = ProfessionalSkill.objects.create(rating_obj=instance)
#         instance.ccr = CharacterConductRatings.objects.create(rating_obj=instance)
        