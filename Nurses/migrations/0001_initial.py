# Generated by Django 3.2.4 on 2021-08-23 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('job_title', models.CharField(blank=True, max_length=255, null=True)),
                ('license_number', models.CharField(max_length=25, unique=True)),
                ('license_state', localflavor.us.models.USStateField(default='OK', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('job_class', models.CharField(blank=True, choices=[('BSN/RN', 'BSN/RN'), ('BSN/LPN', 'BSN/LPN'), ('RN', 'RN'), ('LPN', 'LPN'), ('NP', 'NP'), ('Pharmacist', 'Pharmacist'), ('Other', 'Other'), ('PA', 'PA')], max_length=25, null=True)),
                ('work_experience', models.IntegerField(blank=True, null=True)),
                ('shift', models.CharField(blank=True, choices=[('N', 'Night'), ('Day', 'Day'), ('Both', 'Both')], max_length=10, null=True)),
                ('department', models.CharField(blank=True, max_length=250, null=True)),
                ('other_positions', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
