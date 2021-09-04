# Generated by Django 3.2.4 on 2021-08-23 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('rating_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_centered_care', models.FloatField()),
                ('character_and_conduct', models.FloatField()),
                ('professional_skill', models.FloatField()),
                ('total_average', models.FloatField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctors.doctor')),
            ],
        ),
    ]
