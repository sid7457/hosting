# Generated by Django 3.1.4 on 2021-06-08 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookPublished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=100)),
                ('name_faculty', models.CharField(default='', max_length=100)),
                ('title_of_book', models.CharField(default='', max_length=100)),
                ('name_of_publisher', models.CharField(default='', max_length=100)),
                ('date_publication', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='BTechStudentData',
            fields=[
                ('name', models.CharField(default='', max_length=100)),
                ('PRN', models.CharField(default='', max_length=20, primary_key=True, serialize=False)),
                ('gender', models.CharField(default='', max_length=10)),
                ('address', models.CharField(default='', max_length=200)),
                ('admission_date', models.DateField(default=datetime.date.today)),
                ('category', models.CharField(default='', max_length=40)),
                ('fees_paid', models.PositiveBigIntegerField(default=0)),
                ('branch', models.CharField(default='', max_length=40)),
                ('clg_shift', models.CharField(default='1', max_length=20)),
                ('CET_Score', models.FloatField(default=None)),
                ('admission_type', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyCompletedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=100)),
                ('faculty_name', models.CharField(default='', max_length=100)),
                ('title_course', models.CharField(default='', max_length=100)),
                ('starting_date', models.DateField(default=datetime.date.today)),
                ('completion_date', models.DateField(default=datetime.date.today)),
                ('mode', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=100)),
                ('title', models.CharField(default='', max_length=100)),
                ('name_faculty', models.CharField(default='', max_length=100)),
                ('patent_no', models.IntegerField(default=0)),
                ('date_of_file', models.DateField(default=datetime.date.today)),
                ('awarded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PHD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('department', models.CharField(default='', max_length=20)),
                ('guide_name', models.CharField(default='', max_length=20)),
                ('registration_date', models.DateField(default=datetime.date.today)),
                ('title', models.CharField(default='', max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('completion_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchPaperMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(default='', max_length=20)),
                ('type_of_publication', models.CharField(default='', max_length=20)),
                ('details_of_paper', models.CharField(default='', max_length=200)),
                ('author_name', models.CharField(default='', max_length=200)),
                ('publication_date', models.DateField(default=datetime.date.today)),
                ('department', models.CharField(default='', max_length=20)),
                ('area_of_research', models.CharField(default='', max_length=20)),
                ('publication_details', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchPaperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(default='', max_length=20)),
                ('user', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('name', models.CharField(default='', max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('address1_permanent', models.CharField(default='', max_length=100)),
                ('address2_optional', models.CharField(default='', max_length=100)),
                ('college_post', models.CharField(default='', max_length=20)),
                ('joining_date', models.DateField(default=datetime.date.today)),
                ('teaching_type', models.CharField(default='Degree', max_length=20)),
                ('regular_contractual', models.BooleanField(default=False)),
                ('department', models.CharField(default='', max_length=50)),
                ('higher_education', models.CharField(default='', max_length=100)),
                ('gate_score', models.FloatField(default=None)),
                ('cat_score', models.FloatField(default=None)),
                ('gre_score', models.FloatField(default=None)),
            ],
        ),
    ]
