"""AnnualReport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'ME'
urlpatterns = [
    path('/', include([
        path('teacherHome', views.teacherHome, name='teacherHome'),
        path('teacherProfile', views.teacherProfile, name='teacherProfile'),
        path('editTeacherProfile', views.editTeacherProfile, name='editTeacherProfile'),
        path('changePassword', views.changePassword, name="changePassword"),
        path('researchPapers', views.researchPapers, name='researchPapers'),
        path('addResearchPapers', views.addResearchPapers, name="addResearchPapers"),
        path('researchPaperDelete/<str:doi>', views.researchPaperDelete, name="researchPaperDelete"),
        path('phdDetails', views.phdDetails, name="phdDetails"),
        path('addPHD', views.addPHD, name="addPHD"),
        path('phdDetailsDelete/<str:id>', views.phdDetailsDelete, name="phdDetailsDelete"),
        path('studentData', views.studentData, name="studentData"),
        path('addStudentData', views.addStudentData, name="addStudentData"),
        path('importStudentData', views.importStudentData, name="importStudentData"),
        path('studentDataDelete/<str:PRN>', views.studentDataDelete, name="studentDataDelete"),
        path('bookPublished', views.bookPublished, name="bookPublished"),
        path('addBookPublished', views.addBookPublished, name="addBookPublished"),
        path('bookPublishedDelete/<str:id>', views.bookPublishedDelete, name="bookPublishedDelete"),
        path('patents', views.patents, name="patents"),
        path('addPatents', views.addPatents, name="addPatents"),
        path('patentsDelete/<str:id>', views.patentsDelete, name="patentsDelete"),
        path('facultyCompletedCourse', views.facultyCompletedCourse, name="facultyCompletedCourse"),
        path('addFacultyCompletedCourse', views.addFacultyCompletedCourse, name="addFacultyCompletedCourse"),
        path('facultyCompletedCourseDelete/<str:id>', views.facultyCompletedCourseDelete, name="facultyCompletedCourseDelete"),
        path('guidePhdDetails', views.guidePhdDetails, name="guidePhdDetails"),
        path('addGuidePHD', views.guideAddPHD, name="addGuidePHD"),
        path('guidePhdDetailsDelete/<str:id>', views.guidePhdDetailsDelete, name="guidePhdDetailsDelete"),
        path('googleScholarCitationDetails', views.googleScholarCitationDetails, name="googleScholarCitationDetails"),
        path('addGoogleScholarCitationDetails', views.addGoogleScholarCitationDetails, name="addGoogleScholarCitationDetails"),
        path('googleScholarCitationDetailsDelete/<str:id>', views.googleScholarCitationDetailsDelete, name="googleScholarCitationDetailsDelete"),
        path('guestLecOrganizedOrDelivered', views.guestLecOrganizedOrDelivered, name="guestLecOrganizedOrDelivered"),
        path('addguestLecOrganizedOrDelivered', views.addguestLecOrganizedOrDelivered, name="addguestLecOrganizedOrDelivered"),
        path('guestLecOrganizedOrDeliveredDelete/<str:id>', views.guestLecOrganizedOrDeliveredDelete, name="guestLecOrganizedOrDeliveredDelete"),
        path('eventConductedOrAttended', views.eventConductedOrAttended, name="eventConductedOrAttended"),
        path('addeventConductedOrAttended', views.addeventConductedOrAttended, name="addeventConductedOrAttended"),
        path('eventConductedOrAttendedDelete/<str:id>', views.eventConductedOrAttendedDelete, name="eventConductedOrAttendedDelete"),
    ])),

]
