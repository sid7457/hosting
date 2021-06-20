import datetime

from django.db import models


# Create your models here.


class Teacher(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=20, default="")
    age = models.IntegerField(default=0)
    address1_permanent = models.CharField(max_length=100, default="")
    address2_optional = models.CharField(max_length=100, default="")
    college_post = models.CharField(max_length=20, default="")  # key post in clg
    teaching_type = models.CharField(max_length=20, default="Degree")  # degree/Diploma/Non-teaching
    regular_contractual = models.BooleanField(default=False)  # True-Regular False-contractual
    department = models.CharField(max_length=50, default="")
    higher_education = models.CharField(max_length=100, default="")
    gate_score = models.FloatField(default=None)
    cat_score = models.FloatField(default=None)
    gre_score = models.FloatField(default=None)


class PHD(models.Model):
    user = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=20, default="")
    guide_name = models.CharField(max_length=20, default="")
    registration_date = models.DateField(default=datetime.date.today)  # YYYY-MM-DD
    title = models.CharField(max_length=1000, default="")
    status = models.BooleanField(default=False)  # True-completed False-ongoing
    completion_date = models.DateField(default=datetime.date.today)  # YYYY-MM-DD


class BTechStudentData(models.Model):
    name = models.CharField(max_length=100, default="")
    PRN = models.CharField(max_length=20, primary_key=True, default="")
    gender = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=200, default="")
    category = models.CharField(max_length=40, default="")
    fees_paid = models.PositiveBigIntegerField(default=0)
    branch = models.CharField(max_length=40, default="")
    clg_shift = models.CharField(max_length=20, default="1")
    CET_Score = models.FloatField(default=None)
    admission_type = models.CharField(max_length=20, default="")
    academic_year = models.PositiveBigIntegerField(default=0)


class ResearchPaperMain(models.Model):
    doi = models.CharField(max_length=20, default="")
    type_of_publication = models.CharField(max_length=20, default="")
    details_of_paper = models.CharField(max_length=1000, default="")
    author_name = models.CharField(max_length=200, default="")
    publication_date = models.DateField(default=datetime.date.today)
    department = models.CharField(max_length=20, default="")
    area_of_research = models.CharField(max_length=200, default="")
    publication_details = models.CharField(max_length=1000, default="")
    academic_year = models.PositiveBigIntegerField(default=0)


class ResearchPaperUser(models.Model):
    doi = models.CharField(max_length=20, default="")
    user = models.CharField(max_length=100, default="")


class BookPublished(models.Model):
    user = models.CharField(max_length=100, default="")
    name_faculty = models.CharField(max_length=100, default="")
    title_of_book = models.CharField(max_length=500, default="")
    name_of_publisher = models.CharField(max_length=100, default="")
    date_publication = models.DateField(default=datetime.date.today)
    academic_year = models.PositiveBigIntegerField(default=0)


class Patents(models.Model):
    user = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=500, default="")
    name_faculty = models.CharField(max_length=100, default="")  # possible many name
    patent_no = models.IntegerField(default=0)
    date_of_file = models.DateField(default=datetime.date.today)
    awarded = models.BooleanField(default=False)  # true or false
    academic_year = models.PositiveBigIntegerField(default=0)


class FacultyCompletedCourse(models.Model):
    user = models.CharField(max_length=100, default="")
    faculty_name = models.CharField(max_length=100, default="")
    title_course = models.CharField(max_length=300, default="")
    starting_date = models.DateField(default=datetime.date.today)
    completion_date = models.DateField(default=datetime.date.today)
    mode = models.CharField(max_length=100, default="")
    academic_year = models.PositiveBigIntegerField(default=0)


class GuideforPHD(models.Model):
    user = models.CharField(max_length=100, default="")
    student_name = models.CharField(max_length=100, default="")
    registration_date = models.DateField(default=datetime.date.today)
    title_thesis = models.CharField(max_length=500, default="")
    guide_name = models.CharField(max_length=100, default="")
    comment_on_thesis = models.CharField(max_length=20, default="")
    status = models.BooleanField(default=False)
    completion_date = models.DateField(default=datetime.date.today)
    type_of_phd = models.CharField(max_length=20, default="other")  # QIP and NDF


class GoogleScholarCitationDetails(models.Model):
    user = models.CharField(max_length=100, default="")
    teacher_name = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    citations_2015 = models.IntegerField(default=0)
    h_index_2015 = models.IntegerField(default=0)
    i_10_2015 = models.IntegerField(default=0)
    citations_all = models.IntegerField(default=0)
    h_index_all = models.IntegerField(default=0)
    i_10_all = models.IntegerField(default=0)
    cited_publication = models.IntegerField(default=0)
    reported_publication = models.IntegerField(default=0)
    academic_year = models.PositiveBigIntegerField(default=0)




class GuestLecOrganizedOrDelivered(models.Model):
    user = models.CharField(max_length=100, default="")
    teacher_name = models.CharField(max_length=100, default="")
    place = models.CharField(max_length=100, default="")
    subject = models.CharField(max_length=100, default="")
    starting_date = models.DateField(default=datetime.date.today)
    ending_date = models.DateField(default=datetime.date.today)
    type = models.CharField(max_length=100, default="")         #Organized or Delivered
    academic_year = models.PositiveBigIntegerField(default=0)


class EventConductedOrAttended(models.Model):
    user = models.CharField(max_length=100, default="")
    teacher_name = models.CharField(max_length=100, default="")
    nameof_event = models.CharField(max_length=100, default="")
    event_details = models.CharField(max_length=100, default="")
    starting_date = models.DateField(default=datetime.date.today)
    ending_date = models.DateField(default=datetime.date.today)
    type_of_event = models.CharField(max_length=100, default="")   #conducted or Attended
    academic_year = models.PositiveBigIntegerField(default=0)