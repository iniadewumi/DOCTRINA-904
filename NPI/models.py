from django.db import models

# Create your models here.
class HospitalNPI(models.Model):
    npi_type = models.CharField(max_length=15, default='Organization')
    npi_number = models.IntegerField(primary_key=True)
    enumeration_date = models.DateTimeField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

class DoctorNPI(models.Model):
    npi_type = models.CharField(max_length=15, default='Individual')
    npi_number = models.IntegerField(primary_key=True)
    last_updated = models.DateTimeField(auto_now=True)
    enumeration_date = models.DateTimeField(blank=True)
    
class NurseNPI(models.Model):
    npi_type = models.CharField(max_length=15, default='Individual')
    npi_number = models.IntegerField(primary_key=True)
    last_updated = models.DateTimeField(auto_now=True)
    enumeration_date = models.DateTimeField(blank=True)
    