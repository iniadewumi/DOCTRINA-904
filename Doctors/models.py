from django.db import models
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USStateField, USZipCodeField

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
    )



class UserManager(BaseUserManager):
    def create_user(self):
        pass
#this is just a test
#this is another test
    

class Doctor(models.Model):
    doctor_npi = models.OneToOneField(to='NPI.DoctorNPI', on_delete=models.CASCADE, primary_key=True, unique=True)

    doctor_taxonomy = models.ForeignKey('Taxonomy.DoctorTaxonomy', on_delete=models.DO_NOTHING, related_name='doctaxonomy')
    hospital_system = models.ForeignKey('Hospitals.HospitalSystem', on_delete=models.CASCADE)
    
    # email = models.EmailField(max_length=250, blank=True)

    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150)


    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20, choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    last_updated = models.DateTimeField(auto_now=True)

    credential_text = models.CharField(max_length=5, blank=True, null=True)
    # credential_type = models.CharField(max_length=2)

    doctor_license = models.CharField(max_length=250, blank=True)
    license_state = USStateField()

    sole_proprietor = models.BooleanField()
    status = models.CharField(max_length=10, choices=(('A', 'Active'), ('I', 'Inactive')), default='A')


    years_in_current_hospital = models.IntegerField(null=True)
    experience = models.IntegerField()
    image_url = models.CharField(max_length=200, default="Doctors\static\Pages\images\medical-doctor-profile-icon-male-portrait-flat-design-EY25CP.jpg")

    mailing_address = models.ForeignKey('MailingAddress', on_delete=models.DO_NOTHING, related_name='doctormailing')
    practice_address = models.ForeignKey('PracticeAddress', on_delete=models.DO_NOTHING, related_name='doctorpractice')

    @property
    def model_string(self):
        return f'{self.first_name} {self.area_of_expertise} {self.middle_name} {self.last_name}'

class MailingAddress(models.Model):
    address_id = models.OneToOneField(to='Doctor', on_delete=models.CASCADE, primary_key=True)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True)

    # hospital_state = USStateField(default="OK")
    city = models.CharField(max_length=64, default="Tulsa")
    state = USStateField(default="OK")
    zip_code = USZipCodeField(default="74119")
    
    contact_email = models.EmailField(max_length=250, blank=True, null=True)
    contact_phone = PhoneNumberField(blank=True, null=True)
    fax = PhoneNumberField(blank=True, null=True)

# Create your models here.
class PracticeAddress(models.Model):
    address_id = models.OneToOneField(to='Doctor', on_delete=models.CASCADE, primary_key=True)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True)

    # hospital_state = USStateField(default="OK")
    city = models.CharField(max_length=64, default="Tulsa")
    state = USStateField(default="OK")
    zip_code = USZipCodeField(default="74119")
    
    contact_email = models.EmailField(max_length=250, blank=True, null=True)
    contact_phone = PhoneNumberField(blank=True, null=True)
    fax = PhoneNumberField(blank=True, null=True)

