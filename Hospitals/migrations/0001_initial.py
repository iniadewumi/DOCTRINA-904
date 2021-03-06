# Generated by Django 3.2.4 on 2021-09-17 19:34

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Taxonomy', '0001_initial'),
        ('NPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalSystem',
            fields=[
                ('hospital_npi', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='NPI.hospitalnpi')),
                ('hospital_name', models.CharField(max_length=250)),
                ('image', models.CharField(default='Hospitals\\static\\Pages\\`images\\hospital-building-isometric-3d-pixel-design-icon-vector-5374734.jpg', max_length=200)),
                ('about', models.CharField(max_length=250)),
                ('organization_type_taxonomy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Taxonomy.hospitaltypetaxonomy')),
                ('specialty_taxonomy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Taxonomy.hospitalspectaxonomy')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorizedOfficial',
            fields=[
                ('hosp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Hospitals.hospitalsystem')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='MailingAddress',
            fields=[
                ('hosp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Hospitals.hospitalsystem')),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(default='Tulsa', max_length=64)),
                ('state', localflavor.us.models.USStateField(default='OK', max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(default='74119', max_length=10)),
                ('contact_email', models.EmailField(blank=True, max_length=250, null=True)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='PracticeAddress',
            fields=[
                ('hosp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Hospitals.hospitalsystem')),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(default='Tulsa', max_length=64)),
                ('state', localflavor.us.models.USStateField(default='OK', max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(default='74119', max_length=10)),
                ('contact_email', models.EmailField(blank=True, max_length=250, null=True)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
            ],
        ),
        migrations.AddField(
            model_name='hospitalsystem',
            name='authorized_official',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='Hospitals.authorizedofficial'),
        ),
        migrations.AddField(
            model_name='hospitalsystem',
            name='mailing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Hospitals.mailingaddress'),
        ),
        migrations.AddField(
            model_name='hospitalsystem',
            name='practice_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Hospitals.practiceaddress'),
        ),
    ]
