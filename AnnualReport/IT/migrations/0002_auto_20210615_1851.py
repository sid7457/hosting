# Generated by Django 3.1.4 on 2021-06-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpublished',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='btechstudentdata',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='facultycompletedcourse',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patents',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='phd',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='researchpapermain',
            name='academic_year',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]