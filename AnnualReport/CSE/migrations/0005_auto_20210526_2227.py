# Generated by Django 3.2.3 on 2021-05-26 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0004_researchpapermain_researchpaperuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='address1_permanant',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='address2_optional',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='cat_score',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='teacher',
            name='college_post',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='teacher',
            name='gate_score',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='teacher',
            name='gre_score',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='teacher',
            name='higher_education',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='teacher',
            name='joining_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='regular_contractual',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaching_type',
            field=models.CharField(default='Degree', max_length=20),
        ),
    ]
