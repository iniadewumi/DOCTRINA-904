from django.db import models
# from localflavor.us.forms import USStateSelect

# Create your models here.

class DoctorTaxonomy(models.Model):
    taxonomy_id = models.CharField(max_length=20, primary_key=True, unique=True)
    field_class = models.CharField(max_length=250, null=True)

    medicare_description = models.CharField(max_length=250, null=True)
    specialization = models.CharField(max_length=250, null=True)
    area_of_expertise = models.CharField(max_length=250, null=True)



class HospitalTypeTaxonomy(models.Model):
    taxonomy_id = models.CharField(max_length=20, primary_key=True, unique=True)
    description = models.CharField(max_length=200, null=True)
    
    # state = USStateSelect()


class HospitalSpecTaxonomy(models.Model):
    taxonomy_id = models.CharField(max_length=20, primary_key=True, unique=True)
    field_class = models.CharField(max_length=250, null=True)   
   
    medicare_description = models.CharField(max_length=250, null=True)
    specialization = models.CharField(max_length=250, null=True)
    area_of_expertise = models.CharField(max_length=250, null=True)
    