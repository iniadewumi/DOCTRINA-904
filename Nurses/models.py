from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USStateField, USZipCodeField

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
    )

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, job_title, license_number, license_state, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            license_number = license_number,
            license_state = license_state,
            job_title = job_title,
        )

        user.set_password(password)
        user.active = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name,job_title, license_number, license_state, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name = first_name,
            last_name = last_name,
            license_number = license_number,
            license_state = license_state,
            job_title = job_title
        )
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, job_title, license_number, license_state, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name = first_name,
            last_name = last_name,
            license_number = license_number,
            license_state = license_state,
            job_title = job_title
        )
        user.staff = True
        user.admin = True
        user.active = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
        
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    job_title = models.CharField(max_length=255, blank=True, null=True)

    license_number = models.CharField(max_length=25, unique=True)
    license_state = USStateField(default="OK")
    
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    JOB_CLASSES = (('BSN/RN', 'BSN/RN'),
    ('BSN/LPN', 'BSN/LPN'), 
    ('RN', 'RN'), 
    ('LPN', 'LPN'), 
    ('NP', 'NP'), 
    ('Pharmacist', 'Pharmacist'), 
    ('Other', 'Other'), 
    ('PA', 'PA'))

    job_class = models.CharField(max_length=25, choices=JOB_CLASSES, blank=True, null=True)


    # WORK_EXPERIENCE_C = (
    #     (1, '0-1'),
    #     (3, '1-2'),
    #     (5, '2-5'),
    #     (10, '5-10'),
    #     (11, '10+')        
    # ) 
    work_experience = models.IntegerField(blank=True, null=True)
    shift = models.CharField(max_length=10, choices=(('N', 'Night'), ("Day", "Day"), ('Both', 'Both')), blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    other_positions = models.CharField(max_length=250, null=True, blank=True)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'license_state', 'license_number', 'job_title'] 
    
    objects = UserManager()
    
    def get_full_name(self):
        # The user is identified by their email address
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        # The user is identified by their email address
        return f'{self.first_name[0]}{self.last_name[0]}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


    @property
    def is_active(self):
        "Is the user a admin member?"
        return self.active
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    