from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USStateField, USZipCodeField

# Create your models here.
class HospitalSystem(models.Model):
    hospital_npi = models.OneToOneField(to='NPI.HospitalNPI', on_delete=models.CASCADE, primary_key=True)
    authorized_official = models.OneToOneField(to='AuthorizedOfficial', on_delete=models.DO_NOTHING)

    specialty_taxonomy = models.ForeignKey('Taxonomy.HospitalSpecTaxonomy', on_delete=models.DO_NOTHING, null=True)
    organization_type_taxonomy = models.ForeignKey('Taxonomy.HospitalTypeTaxonomy', on_delete=models.DO_NOTHING, null=True, blank=True)

    hospital_name = models.CharField(max_length=250)
    image = models.CharField(max_length=200, default="Hospitals\static\Pages\`images\hospital-building-isometric-3d-pixel-design-icon-vector-5374734.jpg")
    about = models.CharField(max_length=250)

    mailing_address = models.ForeignKey('MailingAddress', on_delete=models.DO_NOTHING)
    practice_address = models.ForeignKey('PracticeAddress', on_delete=models.DO_NOTHING)


class AuthorizedOfficial(models.Model):
    hosp = models.OneToOneField(to='HospitalSystem', on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title =  models.CharField(max_length=200)
    phone = PhoneNumberField()


class MailingAddress(models.Model):
    hosp = models.OneToOneField(to='HospitalSystem', on_delete=models.CASCADE, primary_key=True)
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
    hosp = models.OneToOneField('HospitalSystem', on_delete=models.CASCADE, primary_key=True)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True)

    # hospital_state = USStateField(default="OK")
    city = models.CharField(max_length=64, default="Tulsa")
    state = USStateField(default="OK")
    zip_code = USZipCodeField(default="74119")
    
    contact_email = models.EmailField(max_length=250, blank=True, null=True)
    contact_phone = PhoneNumberField(blank=True, null=True)
    fax = PhoneNumberField(blank=True, null=True)


    # prac_types = (
    #     ('private', 'Private Practice'),
    #     ('public', 'Public Hospital'),
    #     ('clinic', 'Clinic'),
    #     ('group', 'Group'),

    # )
    # practice_type = models.CharField(max_length=250, choices=prac_types, default="public")

    # tags = (
    #     ('children', 'Children'),
    #     ('cancer', 'Cancer'),
    #     ('rehab', 'Rehabilitation'),
    #     ('general', 'General'),
    #     ('asc', 'Ambulatory Surgery Center')
    # )
    # specialty_tags = models.CharField(max_length=100, choices=tags)

