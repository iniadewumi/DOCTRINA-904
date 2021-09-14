# Generated by Django 3.2.4 on 2021-09-14 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorNPI',
            fields=[
                ('npi_type', models.CharField(default='Individual', max_length=15)),
                ('npi_number', models.IntegerField(primary_key=True, serialize=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('enumeration_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalNPI',
            fields=[
                ('npi_type', models.CharField(default='Organization', max_length=15)),
                ('npi_number', models.IntegerField(primary_key=True, serialize=False)),
                ('enumeration_date', models.DateTimeField(blank=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NurseNPI',
            fields=[
                ('npi_type', models.CharField(default='Individual', max_length=15)),
                ('npi_number', models.IntegerField(primary_key=True, serialize=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('enumeration_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
