# Generated by Django 3.2.4 on 2021-09-05 21:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ratings', '0002_auto_20210824_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anonymous_Comment_and_Whistelblow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anonymous_comment', models.TextField(blank=True, null=True)),
                ('whistelblow', models.BooleanField(default=False)),
                ('whistleblow_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterConductRatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collab', models.BooleanField(default=False)),
                ('accepts_responsibilities', models.BooleanField(default=False)),
                ('like_doc', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralTenants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotional_intelligence', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('effective_patient_communication', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('empathy', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('legal_awareness', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('patient_relationship', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('room_for_improvement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appropriate_diagnosis', models.BooleanField(default=False)),
                ('high_stress_effectiveness', models.BooleanField(default=False)),
                ('communication_to_staff', models.BooleanField(default=False)),
                ('mindful_prescription', models.BooleanField(default=False)),
                ('trust_for_personal_care', models.BooleanField(default=False)),
                ('recommend_regarless_of_personality', models.BooleanField(default=False)),
                ('ethical_practices', models.BooleanField(default=False)),
                ('quality_care', models.BooleanField(default=False)),
                ('improve_care', models.BooleanField(default=False)),
                ('why_improve_care', models.TextField(blank=True, null=True)),
                ('good_patient_outcome', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='profskill',
            name='professional_skill',
        ),
        migrations.RemoveField(
            model_name='patientcare',
            name='patient_centered_care',
        ),
        migrations.AddField(
            model_name='patientcare',
            name='aware_of_rights',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientcare',
            name='communicates_effectively_patients',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientcare',
            name='empathy_to_patient_fam',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientcare',
            name='genuine_patient_care',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientcare',
            name='good_patient_rel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientcare',
            name='recog_psychosocial',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='rating',
            name='patient_centered_care',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Ratings.patientcare'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CharConduct',
        ),
        migrations.DeleteModel(
            name='ProfSkill',
        ),
        migrations.AddField(
            model_name='rating',
            name='anonymous_comment',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Ratings.anonymous_comment_and_whistelblow'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='character_and_conduct',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Ratings.characterconductratings'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='professional_skill',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Ratings.professionalskill'),
            preserve_default=False,
        ),
    ]