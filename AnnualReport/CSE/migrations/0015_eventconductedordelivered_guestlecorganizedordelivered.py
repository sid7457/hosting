# Generated by Django 3.2.3 on 2021-06-18 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0014_remove_btechstudentdata_admission_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventConductedOrDelivered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(default='', max_length=100)),
                ('nameof_event', models.CharField(default='', max_length=100)),
                ('event_details', models.CharField(default='', max_length=100)),
                ('starting_date', models.DateField(default=datetime.date.today)),
                ('ending_date', models.DateField(default=datetime.date.today)),
                ('type_of_event', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GuestLecOrganizedOrDelivered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(default='', max_length=100)),
                ('place', models.CharField(default='', max_length=100)),
                ('subject', models.CharField(default='', max_length=100)),
                ('starting_date', models.DateField(default=datetime.date.today)),
                ('ending_date', models.DateField(default=datetime.date.today)),
                ('type', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
