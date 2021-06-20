
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.template.defaultfilters import register

from AdminApp.utils import render_to_pdf
from CSE.models import ResearchPaperMain as ResearchPaperCSE, BookPublished as BookPublishedCSE, Patents as PatentsCSE, BTechStudentData as BTechStudentDataCSE, PHD as PhdCSE, FacultyCompletedCourse as FacultyCompletedCourseCSE, GuideforPHD as GuideforPHDCSE, GoogleScholarCitationDetails as GoogleScholarCitationDetailsCSE, GuestLecOrganizedOrDelivered as GuestLecOrganizedOrDeliveredCSE, EventConductedOrAttended as EventConductedOrAttendedCSE
from ME.models import ResearchPaperMain as ResearchPaperME, BookPublished as BookPublishedME, Patents as PatentsME, BTechStudentData as BTechStudentDataME, PHD as PhdME, FacultyCompletedCourse as FacultyCompletedCourseME, GuideforPHD as GuideforPHDME, GoogleScholarCitationDetails as GoogleScholarCitationDetailsME, GuestLecOrganizedOrDelivered as GuestLecOrganizedOrDeliveredME, EventConductedOrAttended as EventConductedOrAttendedME
from Civil.models import ResearchPaperMain as ResearchPaperCV, BookPublished as BookPublishedCV, Patents as PatentsCV, BTechStudentData as BTechStudentDataCV, PHD as PhdCV, FacultyCompletedCourse as FacultyCompletedCourseCV, GuideforPHD as GuideforPHDCV, GoogleScholarCitationDetails as GoogleScholarCitationDetailsCV, GuestLecOrganizedOrDelivered as GuestLecOrganizedOrDeliveredCV, EventConductedOrAttended as EventConductedOrAttendedCV
from Electrical.models import ResearchPaperMain as ResearchPaperEL, BookPublished as BookPublishedEL, Patents as PatentsEL, BTechStudentData as BTechStudentDataEL, PHD as PhdEL, FacultyCompletedCourse as FacultyCompletedCourseEL, GuideforPHD as GuideforPHDEL, GoogleScholarCitationDetails as GoogleScholarCitationDetailsEL, GuestLecOrganizedOrDelivered as GuestLecOrganizedOrDeliveredEL, EventConductedOrAttended as EventConductedOrAttendedEL
from Electronics.models import ResearchPaperMain as ResearchPaperETN, BookPublished as BookPublishedETN, Patents as PatentETN, BTechStudentData as BTechStudentDataETN, PHD as PhdETN, FacultyCompletedCourse as FacultyCompletedCourseETN, GuideforPHD as GuideforPHDETN, GoogleScholarCitationDetails as GoogleScholarCitationDetailsETN, GuestLecOrganizedOrDelivered as GuestLecOrganizedOrDeliveredETN, EventConductedOrAttended as EventConductedOrAttendedETN
from IT.models import ResearchPaperMain as ResearchPaperIT, BookPublished as BookPublishedIT, Patents as PatentsIT, BTechStudentData as BTechStudentDataIT, PHD as PhdIT, FacultyCompletedCourse as FacultyCompletedCourseIT, GuideforPHD as GuideforPHDIT, GoogleScholarCitationDetails as GoogleScholarCitationDetailsIT, GuestLecOrganizedOrDelivered as GuestLecOrganizedOrDeliveredIT, EventConductedOrAttended as EventConductedOrAttendedIT

isAdmin = True


def adminHome(request):
    return render(request, "adminHome.html", {"isAdmin": isAdmin})


def generateReport(request):
    if request.method == 'POST':
        fromYear = request.POST.get('fromYear')
        toYear = request.POST.get('toYear')
        st = "generateReportResult/" + fromYear + "/" + toYear
        return redirect(st)

    return render(request, "generateReport.html", {"isAdmin": isAdmin})


def generateReportResult(request, fromYear, toYear):
    toYear = int(toYear)-1
    fromYear = int(fromYear)
    if fromYear > toYear:
        return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")

    # Student Data

    BTechStudentDataCSEGTE96 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataCSEGTE91To95 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataCSEGTE86To90 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataCSEGTE81To85 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataCSEGTE71To80 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataCSEGTELTE70 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataCSEJKSS = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataCSEJKMigrant = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataCSENEUT = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataCSETotal1 = BTechStudentDataCSEGTE96 + BTechStudentDataCSEGTE91To95 + BTechStudentDataCSEGTE86To90 + BTechStudentDataCSEGTE81To85 + BTechStudentDataCSEGTE71To80 + BTechStudentDataCSEGTELTE70
    BTechStudentDataCSETotal2 = BTechStudentDataCSETotal1 + BTechStudentDataCSEJKSS + BTechStudentDataCSEJKMigrant + BTechStudentDataCSENEUT

    BTechStudentDataCVGTE96 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataCVGTE91To95 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataCVGTE86To90 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataCVGTE81To85 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataCVGTE71To80 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataCVGTELTE70 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataCVJKSS = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataCVJKMigrant = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataCVNEUT = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataCVTotal1 = BTechStudentDataCVGTE96 + BTechStudentDataCVGTE91To95 + BTechStudentDataCVGTE86To90 + BTechStudentDataCVGTE81To85 + BTechStudentDataCVGTE71To80 + BTechStudentDataCVGTELTE70
    BTechStudentDataCVTotal2 = BTechStudentDataCVTotal1 + BTechStudentDataCVJKSS + BTechStudentDataCVJKMigrant + BTechStudentDataCVNEUT

    BTechStudentDataMEGTE96 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataMEGTE91To95 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataMEGTE86To90 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataMEGTE81To85 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataMEGTE71To80 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataMEGTELTE70 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataMEJKSS = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataMEJKMigrant = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataMENEUT = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataMETotal1 = BTechStudentDataMEGTE96 + BTechStudentDataMEGTE91To95 + BTechStudentDataMEGTE86To90 + BTechStudentDataMEGTE81To85 + BTechStudentDataMEGTE71To80 + BTechStudentDataMEGTELTE70
    BTechStudentDataMETotal2 = BTechStudentDataMETotal1 + BTechStudentDataMEJKSS + BTechStudentDataMEJKMigrant + BTechStudentDataMENEUT

    BTechStudentDataITGTE96 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataITGTE91To95 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataITGTE86To90 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataITGTE81To85 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataITGTE71To80 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataITGTELTE70 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataITJKSS = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataITJKMigrant = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataITNEUT = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataITTotal1 = BTechStudentDataITGTE96 + BTechStudentDataITGTE91To95 + BTechStudentDataITGTE86To90 + BTechStudentDataITGTE81To85 + BTechStudentDataITGTE71To80 + BTechStudentDataITGTELTE70
    BTechStudentDataITTotal2 = BTechStudentDataITTotal1 + BTechStudentDataITJKSS + BTechStudentDataITJKMigrant + BTechStudentDataITNEUT

    BTechStudentDataELGTE96 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataELGTE91To95 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataELGTE86To90 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataELGTE81To85 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataELGTE71To80 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataELGTELTE70 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataELJKSS = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataELJKMigrant = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataELNEUT = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataELTotal1 = BTechStudentDataELGTE96 + BTechStudentDataELGTE91To95 + BTechStudentDataELGTE86To90 + BTechStudentDataELGTE81To85 + BTechStudentDataELGTE71To80 + BTechStudentDataELGTELTE70
    BTechStudentDataELTotal2 = BTechStudentDataELTotal1 + BTechStudentDataELJKSS + BTechStudentDataELJKMigrant + BTechStudentDataELNEUT

    BTechStudentDataETNGTE96 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataETNGTE91To95 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataETNGTE86To90 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataETNGTE81To85 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataETNGTE71To80 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataETNGTELTE70 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataETNJKSS = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataETNJKMigrant = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataETNNEUT = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataETNTotal1 = BTechStudentDataETNGTE96 + BTechStudentDataETNGTE91To95 + BTechStudentDataETNGTE86To90 + BTechStudentDataETNGTE81To85 + BTechStudentDataETNGTE71To80 + BTechStudentDataETNGTELTE70
    BTechStudentDataETNTotal2 = BTechStudentDataETNTotal1 + BTechStudentDataETNJKSS + BTechStudentDataETNJKMigrant + BTechStudentDataETNNEUT

    # Category Wise Seats List
    BTechStudentDataCSECapSeats = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataCSEWhmtTrust = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataCSEDdTrust = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataCSEEws = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataCSETfws = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataCSEJnK1 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataCSEJnK2 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataCSENri = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataCSEPmsss = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataCSENeut = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataCSECatTotal = BTechStudentDataCSECapSeats + BTechStudentDataCSEWhmtTrust + BTechStudentDataCSEDdTrust + BTechStudentDataCSEEws + BTechStudentDataCSETfws + BTechStudentDataCSEJnK1 + BTechStudentDataCSEJnK2 + BTechStudentDataCSENri + BTechStudentDataCSEPmsss + BTechStudentDataCSENeut

    BTechStudentDataITCapSeats = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataITWhmtTrust = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataITDdTrust = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataITEws = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataITTfws = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataITJnK1 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataITJnK2 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataITNri = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataITPmsss = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataITNeut = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataITCatTotal = BTechStudentDataITCapSeats + BTechStudentDataITWhmtTrust + BTechStudentDataITDdTrust + BTechStudentDataITEws + BTechStudentDataITTfws + BTechStudentDataITJnK1 + BTechStudentDataITJnK2 + BTechStudentDataITNri + BTechStudentDataITPmsss + BTechStudentDataITNeut

    BTechStudentDataCVCapSeats = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataCVWhmtTrust = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataCVDdTrust = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataCVEws = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataCVTfws = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataCVJnK1 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataCVJnK2 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataCVNri = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataCVPmsss = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataCVNeut = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataCVCatTotal = BTechStudentDataCVCapSeats + BTechStudentDataCVWhmtTrust + BTechStudentDataCVDdTrust + BTechStudentDataCVEws + BTechStudentDataCVTfws + BTechStudentDataCVJnK1 + BTechStudentDataCVJnK2 + BTechStudentDataCVNri + BTechStudentDataCVPmsss + BTechStudentDataCVNeut

    BTechStudentDataMECapSeats = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataMEWhmtTrust = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataMEDdTrust = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataMEEws = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataMETfws = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataMEJnK1 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataMEJnK2 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataMENri = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataMEPmsss = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataMENeut = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataMECatTotal = BTechStudentDataMECapSeats + BTechStudentDataMEWhmtTrust + BTechStudentDataMEDdTrust + BTechStudentDataMEEws + BTechStudentDataMETfws + BTechStudentDataMEJnK1 + BTechStudentDataMEJnK2 + BTechStudentDataMENri + BTechStudentDataMEPmsss + BTechStudentDataMENeut

    BTechStudentDataELCapSeats = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataELWhmtTrust = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataELDdTrust = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataELEws = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataELTfws = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataELJnK1 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataELJnK2 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataELNri = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataELPmsss = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataELNeut = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataELCatTotal = BTechStudentDataELCapSeats + BTechStudentDataELWhmtTrust + BTechStudentDataELDdTrust + BTechStudentDataELEws + BTechStudentDataELTfws + BTechStudentDataELJnK1 + BTechStudentDataELJnK2 + BTechStudentDataELNri + BTechStudentDataELPmsss + BTechStudentDataELNeut

    BTechStudentDataETNCapSeats = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataETNWhmtTrust = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataETNDdTrust = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataETNEws = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataETNTfws = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataETNJnK1 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataETNJnK2 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataETNNri = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataETNPmsss = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataETNNeut = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataETNCatTotal = BTechStudentDataETNCapSeats + BTechStudentDataETNWhmtTrust + BTechStudentDataETNDdTrust + BTechStudentDataETNEws + BTechStudentDataETNTfws + BTechStudentDataETNJnK1 + BTechStudentDataETNJnK2 + BTechStudentDataETNNri + BTechStudentDataETNPmsss + BTechStudentDataETNNeut

    # Highest %tile Student

    BTechStudentDataCSEHighestPer = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataCSEHighestPer:
        BTechStudentDataCSEHighestPer = BTechStudentDataCSEHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataCSEHighestPer = 0.0

    BTechStudentDataCVHighestPer = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataCVHighestPer:
        BTechStudentDataCVHighestPer = BTechStudentDataCVHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataCVHighestPer = 0.0

    BTechStudentDataMEHighestPer = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataMEHighestPer:
        BTechStudentDataMEHighestPer = BTechStudentDataMEHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataMEHighestPer = 0.0

    BTechStudentDataITHighestPer = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataITHighestPer:
        BTechStudentDataITHighestPer = BTechStudentDataITHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataITHighestPer = 0.0

    BTechStudentDataELHighestPer = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataELHighestPer:
        BTechStudentDataELHighestPer = BTechStudentDataELHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataELHighestPer = 0.0

    BTechStudentDataETNHighestPer = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataETNHighestPer:
        BTechStudentDataETNHighestPer = BTechStudentDataETNHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataETNHighestPer = 0.0

    # Lowest %tile Student

    BTechStudentDataCSELowestPer = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataCSEHighestPer:
        ab = []
        for i in BTechStudentDataCSELowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataCSELowestPer = res_min
    else:
        BTechStudentDataCSELowestPer = 0.0

    BTechStudentDataCVLowestPer = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataCVHighestPer:
        ab = []
        for i in BTechStudentDataCVLowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataCVLowestPer = res_min
    else:
        BTechStudentDataCVLowestPer = 0.0

    BTechStudentDataMELowestPer = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataMEHighestPer:
        ab = []
        for i in BTechStudentDataMELowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataMELowestPer = res_min
    else:
        BTechStudentDataMELowestPer = 0.0

    BTechStudentDataITLowestPer = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataITHighestPer:
        ab = []
        for i in BTechStudentDataITLowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataITLowestPer = res_min
    else:
        BTechStudentDataITLowestPer = 0.0

    BTechStudentDataELLowestPer = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataELHighestPer:
        ab = []
        for i in BTechStudentDataELLowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataELLowestPer = res_min
    else:
        BTechStudentDataELLowestPer = 0.0

    BTechStudentDataETNLowestPer = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataETNHighestPer:
        ab = []
        for i in BTechStudentDataETNLowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataETNLowestPer = res_min
    else:
        BTechStudentDataETNLowestPer = 0.0

    # Student Gender
    BTechStudentDataCSEMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataCSEFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataCVMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataCVFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataMEMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataMEFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataITMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataITFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataELMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataELFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataETNMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataETNFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    CSETotalMF = BTechStudentDataCSEMale + BTechStudentDataCSEFemale
    CVTotalMF = BTechStudentDataCVMale + BTechStudentDataCVFemale
    ELTotalMF = BTechStudentDataELMale + BTechStudentDataELFemale
    ITTotalMF = BTechStudentDataITMale + BTechStudentDataITFemale
    METotalMF = BTechStudentDataMEMale + BTechStudentDataMEFemale
    ETNTotalMF = BTechStudentDataETNMale + BTechStudentDataETNFemale

    TotalM = BTechStudentDataCSEMale + BTechStudentDataCVMale + BTechStudentDataELMale + BTechStudentDataITMale + BTechStudentDataMEMale + BTechStudentDataETNMale
    TotalF = BTechStudentDataCSEFemale + BTechStudentDataCVFemale + BTechStudentDataELFemale + BTechStudentDataITFemale + BTechStudentDataMEFemale + BTechStudentDataETNFemale

    TotalMF = CSETotalMF + CVTotalMF + ELTotalMF + ITTotalMF + METotalMF + ETNTotalMF

    # Number of Students from Reservation Categories
    BTechStudentDataCSEOpenMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataCSEOpenFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataCSESCMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataCSESCFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataCSESTMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataCSESTFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataCSEVJNTMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataCSEVJNTFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataCSEOBCMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataCSEOBCFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataCSESBCMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataCSESBCFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataCSECatMFTotal = BTechStudentDataCSEOpenMale + BTechStudentDataCSEOpenFemale + BTechStudentDataCSESCMale + BTechStudentDataCSESCFemale + BTechStudentDataCSESTMale + BTechStudentDataCSESTFemale + BTechStudentDataCSEVJNTMale + BTechStudentDataCSEVJNTFemale + BTechStudentDataCSEOBCMale + BTechStudentDataCSEOBCFemale + BTechStudentDataCSESBCMale + BTechStudentDataCSESBCFemale

    BTechStudentDataITOpenMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataITOpenFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataITSCMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataITSCFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataITSTMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataITSTFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataITVJNTMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataITVJNTFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataITOBCMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataITOBCFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataITSBCMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataITSBCFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataITCatMFTotal = BTechStudentDataITOpenMale + BTechStudentDataITOpenFemale + BTechStudentDataITSCMale + BTechStudentDataITSCFemale + BTechStudentDataITSTMale + BTechStudentDataITSTFemale + BTechStudentDataITVJNTMale + BTechStudentDataITVJNTFemale + BTechStudentDataITOBCMale + BTechStudentDataITOBCFemale + BTechStudentDataITSBCMale + BTechStudentDataITSBCFemale

    BTechStudentDataCVOpenMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataCVOpenFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataCVSCMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataCVSCFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataCVSTMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataCVSTFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataCVVJNTMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataCVVJNTFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataCVOBCMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataCVOBCFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataCVSBCMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataCVSBCFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataCVCatMFTotal = BTechStudentDataCVOpenMale + BTechStudentDataCVOpenFemale + BTechStudentDataCVSCMale + BTechStudentDataCVSCFemale + BTechStudentDataCVSTMale + BTechStudentDataCVSTFemale + BTechStudentDataCVVJNTMale + BTechStudentDataCVVJNTFemale + BTechStudentDataCVOBCMale + BTechStudentDataCVOBCFemale + BTechStudentDataCVSBCMale + BTechStudentDataCVSBCFemale

    BTechStudentDataMEOpenMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataMEOpenFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataMESCMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataMESCFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataMESTMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataMESTFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataMEVJNTMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataMEVJNTFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataMEOBCMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataMEOBCFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataMESBCMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataMESBCFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataMECatMFTotal = BTechStudentDataMEOpenMale + BTechStudentDataMEOpenFemale + BTechStudentDataMESCMale + BTechStudentDataMESCFemale + BTechStudentDataMESTMale + BTechStudentDataMESTFemale + BTechStudentDataMEVJNTMale + BTechStudentDataMEVJNTFemale + BTechStudentDataMEOBCMale + BTechStudentDataMEOBCFemale + BTechStudentDataMESBCMale + BTechStudentDataMESBCFemale

    BTechStudentDataELOpenMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataELOpenFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataELSCMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataELSCFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataELSTMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataELSTFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataELVJNTMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataELVJNTFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataELOBCMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataELOBCFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataELSBCMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataELSBCFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataELCatMFTotal = BTechStudentDataELOpenMale + BTechStudentDataELOpenFemale + BTechStudentDataELSCMale + BTechStudentDataELSCFemale + BTechStudentDataELSTMale + BTechStudentDataELSTFemale + BTechStudentDataELVJNTMale + BTechStudentDataELVJNTFemale + BTechStudentDataELOBCMale + BTechStudentDataELOBCFemale + BTechStudentDataELSBCMale + BTechStudentDataELSBCFemale

    BTechStudentDataETNOpenMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataETNOpenFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataETNSCMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataETNSCFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataETNSTMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataETNSTFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataETNVJNTMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataETNVJNTFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataETNOBCMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataETNOBCFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataETNSBCMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataETNSBCFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataETNCatMFTotal = BTechStudentDataETNOpenMale + BTechStudentDataETNOpenFemale + BTechStudentDataETNSCMale + BTechStudentDataETNSCFemale + BTechStudentDataETNSTMale + BTechStudentDataETNSTFemale + BTechStudentDataETNVJNTMale + BTechStudentDataETNVJNTFemale + BTechStudentDataETNOBCMale + BTechStudentDataETNOBCFemale + BTechStudentDataETNSBCMale + BTechStudentDataETNSBCFemale

    # Research Paper
    allResearchPapersCSE = ResearchPaperCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersCV = ResearchPaperCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersME = ResearchPaperME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersIT = ResearchPaperIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersEL = ResearchPaperEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersETN = ResearchPaperETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)

    # Book Published
    allBookPublishedCSE = BookPublishedCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedCV = BookPublishedCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedME = BookPublishedME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedIT = BookPublishedIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedEL = BookPublishedEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedETN = BookPublishedETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)

    # Patents
    allPatentsCSE = PatentsCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsCV = PatentsCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsME = PatentsME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsIT = PatentsIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsEL = PatentsEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsETN = PatentETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)

    # PHD Details - Completed
    allCompletedPHDCSE = PhdCSE.objects.filter(status=True)
    allCompletedPHDIT = PhdIT.objects.filter(status=True)
    allCompletedPHDCV = PhdCV.objects.filter(status=True)
    allCompletedPHDME = PhdME.objects.filter(status=True)
    allCompletedPHDEL = PhdEL.objects.filter(status=True)
    allCompletedPHDETN = PhdETN.objects.filter(status=True)

    # PHD Details - Ongoing
    allOngoingPHDCSE = PhdCSE.objects.filter(status=False)
    allOngoingPHDME = PhdME.objects.filter(status=False)
    allOngoingPHDCV = PhdCV.objects.filter(status=False)
    allOngoingPHDIT = PhdIT.objects.filter(status=False)
    allOngoingPHDEL = PhdEL.objects.filter(status=False)
    allOngoingPHDETN = PhdETN.objects.filter(status=False)

    # Faculty Completed Courses
    allFacCompCourseCSE = FacultyCompletedCourseCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseME = FacultyCompletedCourseME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseCV = FacultyCompletedCourseCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseIT = FacultyCompletedCourseIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseEL = FacultyCompletedCourseEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseETN = FacultyCompletedCourseETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")

    # Ph.D.Student Details registered under WCE faculty(other than QIP - Ph.D. and NDF students)
    allPhdStudentOtherCSE = GuideforPHDCSE.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherME = GuideforPHDME.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherIT = GuideforPHDIT.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherCV = GuideforPHDCV.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherEL = GuideforPHDEL.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherETN = GuideforPHDETN.objects.filter(type_of_phd="Other").order_by("guide_name")

    # Ph.D.Student Details registered under WCE faculty(QIP - Ph.D. students)
    allPhdStudentQIPCSE = GuideforPHDCSE.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPME = GuideforPHDME.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPIT = GuideforPHDIT.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPCV = GuideforPHDCV.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPEL = GuideforPHDEL.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPETN = GuideforPHDETN.objects.filter(type_of_phd="QIP").order_by("guide_name")

    # Ph.D.Student Details registered under WCE faculty(NDF Ph.D. students)
    allPhdStudentNDFCSE = GuideforPHDCSE.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFME = GuideforPHDME.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFIT = GuideforPHDIT.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFCV = GuideforPHDCV.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFEL = GuideforPHDEL.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFETN = GuideforPHDETN.objects.filter(type_of_phd="NDF").order_by("guide_name")

    # Google Scholar Citation Details
    allGoogleCitationCSE = GoogleScholarCitationDetailsCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationIT = GoogleScholarCitationDetailsIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationCV = GoogleScholarCitationDetailsCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationME = GoogleScholarCitationDetailsME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationEL = GoogleScholarCitationDetailsEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationETN = GoogleScholarCitationDetailsETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)

    # Guest Lecture Organized by Faculty
    allGuestLecOrganizedCSE = GuestLecOrganizedOrDeliveredCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedIT = GuestLecOrganizedOrDeliveredIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedME = GuestLecOrganizedOrDeliveredME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedCV = GuestLecOrganizedOrDeliveredCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedEL = GuestLecOrganizedOrDeliveredEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedETN = GuestLecOrganizedOrDeliveredETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")

    # Guest Lecture Delivered by Faculty
    allGuestLecDeliveredCSE = GuestLecOrganizedOrDeliveredCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredIT = GuestLecOrganizedOrDeliveredIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredME = GuestLecOrganizedOrDeliveredME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredCV = GuestLecOrganizedOrDeliveredCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredEL = GuestLecOrganizedOrDeliveredEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredETN = GuestLecOrganizedOrDeliveredETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")

    # Activities Conducted
    allEventConductedCSE = EventConductedOrAttendedCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedIT = EventConductedOrAttendedIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedME = EventConductedOrAttendedME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedCV = EventConductedOrAttendedCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedEL = EventConductedOrAttendedEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedETN = EventConductedOrAttendedETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")

    # Events Attended by Faculty
    allEventAttendedCSE = EventConductedOrAttendedCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedIT = EventConductedOrAttendedIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedME = EventConductedOrAttendedME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedCV = EventConductedOrAttendedCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedEL = EventConductedOrAttendedEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedETN = EventConductedOrAttendedETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")

    # For Displaying Serial No Research Paper
    SerialNoRSPCSE = []
    for i in range(len(allResearchPapersCSE)):
        SerialNoRSPCSE.insert(i, i+1)
    SerialNoRSPIT = []
    for i in range(len(allResearchPapersIT)):
        SerialNoRSPIT.insert(i, i+1)
    SerialNoRSPME = []
    for i in range(len(allResearchPapersME)):
        SerialNoRSPME.insert(i, i+1)
    SerialNoRSPCV = []
    for i in range(len(allResearchPapersCV)):
        SerialNoRSPCV.insert(i, i+1)
    SerialNoRSPEL = []
    for i in range(len(allResearchPapersEL)):
        SerialNoRSPEL.insert(i, i+1)
    SerialNoRSPETN = []
    for i in range(len(allResearchPapersETN)):
        SerialNoRSPETN.insert(i, i+1)

    # For Displaying Serial No Completed PHD
    SerialNoPHDETN = []
    for i in range(len(allCompletedPHDETN)):
        SerialNoPHDETN.insert(i, i + 1)
    c = len(allCompletedPHDETN) + len(allCompletedPHDCV)
    SerialNoPHDCV = []
    for i in range(len(allCompletedPHDETN), c):
        SerialNoPHDCV.insert(i, i + 1)
    SerialNoPHDME = []
    for i in range(c, len(allCompletedPHDME)+c):
        SerialNoPHDME.insert(i, i + 1)
    c += len(allCompletedPHDME)
    SerialNoPHDEL = []
    for i in range(c, len(allCompletedPHDEL)+c):
        SerialNoPHDEL.insert(i, i + 1)
    c += len(allCompletedPHDEL)
    SerialNoPHDIT = []
    for i in range(c, len(allCompletedPHDIT)+c):
        SerialNoPHDIT.insert(i, i + 1)
    c += len(allCompletedPHDIT)
    SerialNoPHDCSE = []
    for i in range(c, len(allCompletedPHDCSE)+c):
        SerialNoPHDCSE.insert(i, i + 1)

    # For Displaying Serial No Ongoing PHD
    SerialNoOngoingPHDETN = []
    for i in range(len(allOngoingPHDETN)):
        SerialNoOngoingPHDETN.insert(i, i + 1)
    c = len(allOngoingPHDETN) + len(allOngoingPHDCV)
    SerialNoOngoingPHDCV = []
    for i in range(len(allOngoingPHDETN), c):
        SerialNoOngoingPHDCV.insert(i, i + 1)
    SerialNoOngoingPHDME = []
    for i in range(c, len(allOngoingPHDME) + c):
        SerialNoOngoingPHDME.insert(i, i + 1)
    c += len(allOngoingPHDME)
    SerialNoOngoingPHDEL = []
    for i in range(c, len(allOngoingPHDEL) + c):
        SerialNoOngoingPHDEL.insert(i, i + 1)
    c += len(allOngoingPHDEL)
    SerialNoOngoingPHDIT = []
    for i in range(c, len(allOngoingPHDIT) + c):
        SerialNoOngoingPHDIT.insert(i, i + 1)
    c += len(allOngoingPHDIT)
    SerialNoOngoingPHDCSE = []
    for i in range(c, len(allOngoingPHDCSE) + c):
        SerialNoOngoingPHDCSE.insert(i, i + 1)

    # For Displaying Serial No Book Published
    SerialNoBookPublishedETN = []
    for i in range(len(allBookPublishedETN)):
        SerialNoBookPublishedETN.insert(i, i + 1)
    c = len(allBookPublishedETN) + len(allBookPublishedCV)
    SerialNoBookPublishedCV = []
    for i in range(len(allBookPublishedETN), c):
        SerialNoBookPublishedCV.insert(i, i + 1)
    SerialNoBookPublishedME = []
    for i in range(c, len(allBookPublishedME) + c):
        SerialNoBookPublishedME.insert(i, i + 1)
    c += len(allBookPublishedME)
    SerialNoBookPublishedEL = []
    for i in range(c, len(allBookPublishedEL) + c):
        SerialNoBookPublishedEL.insert(i, i + 1)
    c += len(allBookPublishedEL)
    SerialNoBookPublishedIT = []
    for i in range(c, len(allBookPublishedIT) + c):
        SerialNoBookPublishedIT.insert(i, i + 1)
    c += len(allBookPublishedIT)
    SerialNoBookPublishedCSE = []
    for i in range(c, len(allBookPublishedCSE) + c):
        SerialNoBookPublishedCSE.insert(i, i + 1)

    # For Displaying Serial No Faculty Completed Courses
    SerialNoFacCompCourseETN = []
    for i in range(len(allFacCompCourseETN)):
        SerialNoFacCompCourseETN.insert(i, i + 1)
    c = len(allFacCompCourseETN) + len(allFacCompCourseCV)
    SerialNoFacCompCourseCV = []
    for i in range(len(allFacCompCourseETN), c):
        SerialNoFacCompCourseCV.insert(i, i + 1)
    SerialNoFacCompCourseME = []
    for i in range(c, len(allFacCompCourseME) + c):
        SerialNoFacCompCourseME.insert(i, i + 1)
    c += len(allFacCompCourseME)
    SerialNoFacCompCourseEL = []
    for i in range(c, len(allFacCompCourseEL) + c):
        SerialNoFacCompCourseEL.insert(i, i + 1)
    c += len(allFacCompCourseEL)
    SerialNoFacCompCourseIT = []
    for i in range(c, len(allFacCompCourseIT) + c):
        SerialNoFacCompCourseIT.insert(i, i + 1)
    c += len(allFacCompCourseIT)
    SerialNoFacCompCourseCSE = []
    for i in range(c, len(allFacCompCourseCSE) + c):
        SerialNoFacCompCourseCSE.insert(i, i + 1)

    # For Displaying Serial No Ph.D.Student Details registered under WCE faculty(other than QIP - Ph.D. and NDF students)
    SerialNoPhdStudentOtherETN = []
    for i in range(len(allPhdStudentOtherETN)):
        SerialNoPhdStudentOtherETN.insert(i, i + 1)
    c = len(allPhdStudentOtherETN) + len(allPhdStudentOtherCV)
    SerialNoPhdStudentOtherCV = []
    for i in range(len(allPhdStudentOtherETN), c):
        SerialNoPhdStudentOtherCV.insert(i, i + 1)
    SerialNoPhdStudentOtherME = []
    for i in range(c, len(allPhdStudentOtherME) + c):
        SerialNoPhdStudentOtherME.insert(i, i + 1)
    c += len(allPhdStudentOtherME)
    SerialNoPhdStudentOtherEL = []
    for i in range(c, len(allPhdStudentOtherEL) + c):
        SerialNoPhdStudentOtherEL.insert(i, i + 1)
    c += len(allPhdStudentOtherEL)
    SerialNoPhdStudentOtherIT = []
    for i in range(c, len(allPhdStudentOtherIT) + c):
        SerialNoPhdStudentOtherIT.insert(i, i + 1)
    c += len(allPhdStudentOtherIT)
    SerialNoPhdStudentOtherCSE = []
    for i in range(c, len(allPhdStudentOtherCSE) + c):
        SerialNoPhdStudentOtherCSE.insert(i, i + 1)

    # For Displaying Serial No Ph.D.Student Details registered under WCE faculty(QIP - Ph.D. students)
    SerialNoPhdStudentQIPETN = []
    for i in range(len(allPhdStudentQIPETN)):
        SerialNoPhdStudentQIPETN.insert(i, i + 1)
    c = len(allPhdStudentQIPETN) + len(allPhdStudentQIPCV)
    SerialNoPhdStudentQIPCV = []
    for i in range(len(allPhdStudentQIPETN), c):
        SerialNoPhdStudentQIPCV.insert(i, i + 1)
    SerialNoPhdStudentQIPME = []
    for i in range(c, len(allPhdStudentQIPME) + c):
        SerialNoPhdStudentQIPME.insert(i, i + 1)
    c += len(allPhdStudentQIPME)
    SerialNoPhdStudentQIPEL = []
    for i in range(c, len(allPhdStudentQIPEL) + c):
        SerialNoPhdStudentQIPEL.insert(i, i + 1)
    c += len(allPhdStudentQIPEL)
    SerialNoPhdStudentQIPIT = []
    for i in range(c, len(allPhdStudentQIPIT) + c):
        SerialNoPhdStudentQIPIT.insert(i, i + 1)
    c += len(allPhdStudentQIPIT)
    SerialNoPhdStudentQIPCSE = []
    for i in range(c, len(allPhdStudentQIPCSE) + c):
        SerialNoPhdStudentQIPCSE.insert(i, i + 1)

    # For Displaying Serial No Ph.D.Student Details registered under WCE faculty(NDF Ph.D. students)
    SerialNoPhdStudentNDFETN = []
    for i in range(len(allPhdStudentNDFETN)):
        SerialNoPhdStudentNDFETN.insert(i, i + 1)
    c = len(allPhdStudentNDFETN) + len(allPhdStudentNDFCV)
    SerialNoPhdStudentNDFCV = []
    for i in range(len(allPhdStudentNDFETN), c):
        SerialNoPhdStudentNDFCV.insert(i, i + 1)
    SerialNoPhdStudentNDFME = []
    for i in range(c, len(allPhdStudentNDFME) + c):
        SerialNoPhdStudentNDFME.insert(i, i + 1)
    c += len(allPhdStudentNDFME)
    SerialNoPhdStudentNDFEL = []
    for i in range(c, len(allPhdStudentNDFEL) + c):
        SerialNoPhdStudentNDFEL.insert(i, i + 1)
    c += len(allPhdStudentNDFEL)
    SerialNoPhdStudentNDFIT = []
    for i in range(c, len(allPhdStudentNDFIT) + c):
        SerialNoPhdStudentNDFIT.insert(i, i + 1)
    c += len(allPhdStudentNDFIT)
    SerialNoPhdStudentNDFCSE = []
    for i in range(c, len(allPhdStudentNDFCSE) + c):
        SerialNoPhdStudentNDFCSE.insert(i, i + 1)


    # Passing args to template for displaying data
    args = {
        "BTechStudentDataCSEGTE96": BTechStudentDataCSEGTE96,
        "BTechStudentDataCSEGTE91To95": BTechStudentDataCSEGTE91To95,
        "BTechStudentDataCSEGTE86To90": BTechStudentDataCSEGTE86To90,
        "BTechStudentDataCSEGTE81To85": BTechStudentDataCSEGTE81To85,
        "BTechStudentDataCSEGTE71To80": BTechStudentDataCSEGTE71To80,
        "BTechStudentDataCSEGTELTE70": BTechStudentDataCSEGTELTE70,
        "BTechStudentDataCSEJKSS": BTechStudentDataCSEJKSS,
        "BTechStudentDataCSEJKMigrant": BTechStudentDataCSEJKMigrant,
        "BTechStudentDataCSENEUT": BTechStudentDataCSENEUT,
        "BTechStudentDataCSETotal1": BTechStudentDataCSETotal1,
        "BTechStudentDataCSETotal2": BTechStudentDataCSETotal2,

        "BTechStudentDataCVGTE96": BTechStudentDataCVGTE96,
        "BTechStudentDataCVGTE91To95": BTechStudentDataCVGTE91To95,
        "BTechStudentDataCVGTE86To90": BTechStudentDataCVGTE86To90,
        "BTechStudentDataCVGTE81To85": BTechStudentDataCVGTE81To85,
        "BTechStudentDataCVGTE71To80": BTechStudentDataCVGTE71To80,
        "BTechStudentDataCVGTELTE70": BTechStudentDataCVGTELTE70,
        "BTechStudentDataCVJKSS": BTechStudentDataCVJKSS,
        "BTechStudentDataCVJKMigrant": BTechStudentDataCVJKMigrant,
        "BTechStudentDataCVNEUT": BTechStudentDataCVNEUT,
        "BTechStudentDataCVTotal1": BTechStudentDataCVTotal1,
        "BTechStudentDataCVTotal2": BTechStudentDataCVTotal2,

        "BTechStudentDataITGTE96": BTechStudentDataITGTE96,
        "BTechStudentDataITGTE91To95": BTechStudentDataITGTE91To95,
        "BTechStudentDataITGTE86To90": BTechStudentDataITGTE86To90,
        "BTechStudentDataITGTE81To85": BTechStudentDataITGTE81To85,
        "BTechStudentDataITGTE71To80": BTechStudentDataITGTE71To80,
        "BTechStudentDataITGTELTE70": BTechStudentDataITGTELTE70,
        "BTechStudentDataITJKSS": BTechStudentDataITJKSS,
        "BTechStudentDataITJKMigrant": BTechStudentDataITJKMigrant,
        "BTechStudentDataITNEUT": BTechStudentDataITNEUT,
        "BTechStudentDataITTotal1": BTechStudentDataITTotal1,
        "BTechStudentDataITTotal2": BTechStudentDataITTotal2,

        "BTechStudentDataMEGTE96": BTechStudentDataMEGTE96,
        "BTechStudentDataMEGTE91To95": BTechStudentDataMEGTE91To95,
        "BTechStudentDataMEGTE86To90": BTechStudentDataMEGTE86To90,
        "BTechStudentDataMEGTE81To85": BTechStudentDataMEGTE81To85,
        "BTechStudentDataMEGTE71To80": BTechStudentDataMEGTE71To80,
        "BTechStudentDataMEGTELTE70": BTechStudentDataMEGTELTE70,
        "BTechStudentDataMEJKSS": BTechStudentDataMEJKSS,
        "BTechStudentDataMEJKMigrant": BTechStudentDataMEJKMigrant,
        "BTechStudentDataMENEUT": BTechStudentDataMENEUT,
        "BTechStudentDataMETotal1": BTechStudentDataMETotal1,
        "BTechStudentDataMETotal2": BTechStudentDataMETotal2,

        "BTechStudentDataELGTE96": BTechStudentDataELGTE96,
        "BTechStudentDataELGTE91To95": BTechStudentDataELGTE91To95,
        "BTechStudentDataELGTE86To90": BTechStudentDataELGTE86To90,
        "BTechStudentDataELGTE81To85": BTechStudentDataELGTE81To85,
        "BTechStudentDataELGTE71To80": BTechStudentDataELGTE71To80,
        "BTechStudentDataELGTELTE70": BTechStudentDataELGTELTE70,
        "BTechStudentDataELJKSS": BTechStudentDataELJKSS,
        "BTechStudentDataELJKMigrant": BTechStudentDataELJKMigrant,
        "BTechStudentDataELNEUT": BTechStudentDataELNEUT,
        "BTechStudentDataELTotal1": BTechStudentDataELTotal1,
        "BTechStudentDataELTotal2": BTechStudentDataELTotal2,

        "BTechStudentDataETNGTE96": BTechStudentDataETNGTE96,
        "BTechStudentDataETNGTE91To95": BTechStudentDataETNGTE91To95,
        "BTechStudentDataETNGTE86To90": BTechStudentDataETNGTE86To90,
        "BTechStudentDataETNGTE81To85": BTechStudentDataETNGTE81To85,
        "BTechStudentDataETNGTE71To80": BTechStudentDataETNGTE71To80,
        "BTechStudentDataETNGTELTE70": BTechStudentDataETNGTELTE70,
        "BTechStudentDataETNJKSS": BTechStudentDataETNJKSS,
        "BTechStudentDataETNJKMigrant": BTechStudentDataETNJKMigrant,
        "BTechStudentDataETNNEUT": BTechStudentDataETNNEUT,
        "BTechStudentDataETNTotal1": BTechStudentDataETNTotal1,
        "BTechStudentDataETNTotal2": BTechStudentDataETNTotal2,

        "BTechStudentDataCSECapSeats": BTechStudentDataCSECapSeats,
        "BTechStudentDataCSEWhmtTrust": BTechStudentDataCSEWhmtTrust,
        "BTechStudentDataCSEDdTrust": BTechStudentDataCSEDdTrust,
        "BTechStudentDataCSEEws": BTechStudentDataCSEEws,
        "BTechStudentDataCSETfws": BTechStudentDataCSETfws,
        "BTechStudentDataCSEJnK1": BTechStudentDataCSEJnK1,
        "BTechStudentDataCSEJnK2": BTechStudentDataCSEJnK2,
        "BTechStudentDataCSENri": BTechStudentDataCSENri,
        "BTechStudentDataCSEPmsss": BTechStudentDataCSEPmsss,
        "BTechStudentDataCSENeut": BTechStudentDataCSENeut,
        "BTechStudentDataCSECatTotal": BTechStudentDataCSECatTotal,

        "BTechStudentDataCVCapSeats": BTechStudentDataCVCapSeats,
        "BTechStudentDataCVWhmtTrust": BTechStudentDataCVWhmtTrust,
        "BTechStudentDataCVDdTrust": BTechStudentDataCVDdTrust,
        "BTechStudentDataCVEws": BTechStudentDataCVEws,
        "BTechStudentDataCVTfws": BTechStudentDataCVTfws,
        "BTechStudentDataCVJnK1": BTechStudentDataCVJnK1,
        "BTechStudentDataCVJnK2": BTechStudentDataCVJnK2,
        "BTechStudentDataCVNri": BTechStudentDataCVNri,
        "BTechStudentDataCVPmsss": BTechStudentDataCVPmsss,
        "BTechStudentDataCVNeut": BTechStudentDataCVNeut,
        "BTechStudentDataCVCatTotal": BTechStudentDataCVCatTotal,

        "BTechStudentDataITCapSeats": BTechStudentDataITCapSeats,
        "BTechStudentDataITWhmtTrust": BTechStudentDataITWhmtTrust,
        "BTechStudentDataITDdTrust": BTechStudentDataITDdTrust,
        "BTechStudentDataITEws": BTechStudentDataITEws,
        "BTechStudentDataITTfws": BTechStudentDataITTfws,
        "BTechStudentDataITJnK1": BTechStudentDataITJnK1,
        "BTechStudentDataITJnK2": BTechStudentDataITJnK2,
        "BTechStudentDataITNri": BTechStudentDataITNri,
        "BTechStudentDataITPmsss": BTechStudentDataITPmsss,
        "BTechStudentDataITNeut": BTechStudentDataITNeut,
        "BTechStudentDataITCatTotal": BTechStudentDataITCatTotal,

        "BTechStudentDataMECapSeats": BTechStudentDataMECapSeats,
        "BTechStudentDataMEWhmtTrust": BTechStudentDataMEWhmtTrust,
        "BTechStudentDataMEDdTrust": BTechStudentDataMEDdTrust,
        "BTechStudentDataMEEws": BTechStudentDataMEEws,
        "BTechStudentDataMETfws": BTechStudentDataMETfws,
        "BTechStudentDataMEJnK1": BTechStudentDataMEJnK1,
        "BTechStudentDataMEJnK2": BTechStudentDataMEJnK2,
        "BTechStudentDataMENri": BTechStudentDataMENri,
        "BTechStudentDataMEPmsss": BTechStudentDataMEPmsss,
        "BTechStudentDataMENeut": BTechStudentDataMENeut,
        "BTechStudentDataMECatTotal": BTechStudentDataMECatTotal,

        "BTechStudentDataELCapSeats": BTechStudentDataELCapSeats,
        "BTechStudentDataELWhmtTrust": BTechStudentDataELWhmtTrust,
        "BTechStudentDataELDdTrust": BTechStudentDataELDdTrust,
        "BTechStudentDataELEws": BTechStudentDataELEws,
        "BTechStudentDataELTfws": BTechStudentDataELTfws,
        "BTechStudentDataELJnK1": BTechStudentDataELJnK1,
        "BTechStudentDataELJnK2": BTechStudentDataELJnK2,
        "BTechStudentDataELNri": BTechStudentDataELNri,
        "BTechStudentDataELPmsss": BTechStudentDataELPmsss,
        "BTechStudentDataELNeut": BTechStudentDataELNeut,
        "BTechStudentDataELCatTotal": BTechStudentDataELCatTotal,

        "BTechStudentDataETNCapSeats": BTechStudentDataETNCapSeats,
        "BTechStudentDataETNWhmtTrust": BTechStudentDataETNWhmtTrust,
        "BTechStudentDataETNDdTrust": BTechStudentDataETNDdTrust,
        "BTechStudentDataETNEws": BTechStudentDataETNEws,
        "BTechStudentDataETNTfws": BTechStudentDataETNTfws,
        "BTechStudentDataETNJnK1": BTechStudentDataETNJnK1,
        "BTechStudentDataETNJnK2": BTechStudentDataETNJnK2,
        "BTechStudentDataETNNri": BTechStudentDataETNNri,
        "BTechStudentDataETNPmsss": BTechStudentDataETNPmsss,
        "BTechStudentDataETNNeut": BTechStudentDataETNNeut,
        "BTechStudentDataETNCatTotal": BTechStudentDataETNCatTotal,

        "BTechStudentDataTotalCapSeats": BTechStudentDataCVCapSeats + BTechStudentDataETNCapSeats + BTechStudentDataELCapSeats + BTechStudentDataMECapSeats + BTechStudentDataITCapSeats + BTechStudentDataCSECapSeats,
        "BTechStudentDataTotalWhmtTrust": BTechStudentDataCVWhmtTrust + BTechStudentDataETNWhmtTrust + BTechStudentDataELWhmtTrust + BTechStudentDataMEWhmtTrust + BTechStudentDataITWhmtTrust + BTechStudentDataCSEWhmtTrust,
        "BTechStudentDataTotalDdTrust": BTechStudentDataCVDdTrust + BTechStudentDataETNDdTrust + BTechStudentDataELDdTrust + BTechStudentDataMEDdTrust + BTechStudentDataITDdTrust + BTechStudentDataCSEDdTrust,
        "BTechStudentDataTotalEws": BTechStudentDataCVEws + BTechStudentDataETNEws + BTechStudentDataELEws + BTechStudentDataMEEws + BTechStudentDataITEws + BTechStudentDataCSEEws,
        "BTechStudentDataTotalTfws": BTechStudentDataCVTfws + BTechStudentDataETNTfws + BTechStudentDataELTfws + BTechStudentDataMETfws + BTechStudentDataITTfws + BTechStudentDataCSETfws,
        "BTechStudentDataTotalJnK1": BTechStudentDataCVJnK1 + BTechStudentDataETNJnK1 + BTechStudentDataELJnK1 + BTechStudentDataMEJnK1 + BTechStudentDataITJnK1 + BTechStudentDataCSEJnK1,
        "BTechStudentDataTotalJnK2": BTechStudentDataCVJnK2 + BTechStudentDataETNJnK2 + BTechStudentDataELJnK2 + BTechStudentDataMEJnK2 + BTechStudentDataITJnK2 + BTechStudentDataCSEJnK2,
        "BTechStudentDataTotalNri": BTechStudentDataCVNri + BTechStudentDataETNNri + BTechStudentDataELNri + BTechStudentDataMENri + BTechStudentDataITNri + BTechStudentDataCSENri,
        "BTechStudentDataTotalPmsss": BTechStudentDataCVPmsss + BTechStudentDataETNPmsss + BTechStudentDataELPmsss + BTechStudentDataMEPmsss + BTechStudentDataITPmsss + BTechStudentDataCSEPmsss,
        "BTechStudentDataTotalNeut": BTechStudentDataCVNeut + BTechStudentDataETNNeut + BTechStudentDataELNeut + BTechStudentDataMENeut + BTechStudentDataITNeut + BTechStudentDataCSENeut,
        "BTechStudentDataTotalCatTotal": BTechStudentDataCVCatTotal + BTechStudentDataETNCatTotal + BTechStudentDataELCatTotal + BTechStudentDataMECatTotal + BTechStudentDataITCatTotal + BTechStudentDataCSECatTotal,

        "BTechStudentDataCSEOpenMale": BTechStudentDataCSEOpenMale,
        "BTechStudentDataCSEOpenFemale": BTechStudentDataCSEOpenFemale,
        "BTechStudentDataCSESCMale": BTechStudentDataCSESCMale,
        "BTechStudentDataCSESCFemale": BTechStudentDataCSESCFemale,
        "BTechStudentDataCSESTMale": BTechStudentDataCSESTMale,
        "BTechStudentDataCSESTFemale": BTechStudentDataCSESTFemale,
        "BTechStudentDataCSEVJNTMale": BTechStudentDataCSEVJNTMale,
        "BTechStudentDataCSEVJNTFemale": BTechStudentDataCSEVJNTFemale,
        "BTechStudentDataCSEOBCMale": BTechStudentDataCSEOBCMale,
        "BTechStudentDataCSEOBCFemale": BTechStudentDataCSEOBCFemale,
        "BTechStudentDataCSESBCMale": BTechStudentDataCSESBCMale,
        "BTechStudentDataCSESBCFemale": BTechStudentDataCSESBCFemale,
        "BTechStudentDataCSECatMFTotal": BTechStudentDataCSECatMFTotal,

        "BTechStudentDataITOpenMale": BTechStudentDataITOpenMale,
        "BTechStudentDataITOpenFemale": BTechStudentDataITOpenFemale,
        "BTechStudentDataITSCMale": BTechStudentDataITSCMale,
        "BTechStudentDataITSCFemale": BTechStudentDataITSCFemale,
        "BTechStudentDataITSTMale": BTechStudentDataITSTMale,
        "BTechStudentDataITSTFemale": BTechStudentDataITSTFemale,
        "BTechStudentDataITVJNTMale": BTechStudentDataITVJNTMale,
        "BTechStudentDataITVJNTFemale": BTechStudentDataITVJNTFemale,
        "BTechStudentDataITOBCMale": BTechStudentDataITOBCMale,
        "BTechStudentDataITOBCFemale": BTechStudentDataITOBCFemale,
        "BTechStudentDataITSBCMale": BTechStudentDataITSBCMale,
        "BTechStudentDataITSBCFemale": BTechStudentDataITSBCFemale,
        "BTechStudentDataITCatMFTotal": BTechStudentDataITCatMFTotal,

        "BTechStudentDataCVOpenMale": BTechStudentDataCVOpenMale,
        "BTechStudentDataCVOpenFemale": BTechStudentDataCVOpenFemale,
        "BTechStudentDataCVSCMale": BTechStudentDataCVSCMale,
        "BTechStudentDataCVSCFemale": BTechStudentDataCVSCFemale,
        "BTechStudentDataCVSTMale": BTechStudentDataCVSTMale,
        "BTechStudentDataCVSTFemale": BTechStudentDataCVSTFemale,
        "BTechStudentDataCVVJNTMale": BTechStudentDataCVVJNTMale,
        "BTechStudentDataCVVJNTFemale": BTechStudentDataCVVJNTFemale,
        "BTechStudentDataCVOBCMale": BTechStudentDataCVOBCMale,
        "BTechStudentDataCVOBCFemale": BTechStudentDataCVOBCFemale,
        "BTechStudentDataCVSBCMale": BTechStudentDataCVSBCMale,
        "BTechStudentDataCVSBCFemale": BTechStudentDataCVSBCFemale,
        "BTechStudentDataCVCatMFTotal": BTechStudentDataCVCatMFTotal,

        "BTechStudentDataMEOpenMale": BTechStudentDataMEOpenMale,
        "BTechStudentDataMEOpenFemale": BTechStudentDataMEOpenFemale,
        "BTechStudentDataMESCMale": BTechStudentDataMESCMale,
        "BTechStudentDataMESCFemale": BTechStudentDataMESCFemale,
        "BTechStudentDataMESTMale": BTechStudentDataMESTMale,
        "BTechStudentDataMESTFemale": BTechStudentDataMESTFemale,
        "BTechStudentDataMEVJNTMale": BTechStudentDataMEVJNTMale,
        "BTechStudentDataMEVJNTFemale": BTechStudentDataMEVJNTFemale,
        "BTechStudentDataMEOBCMale": BTechStudentDataMEOBCMale,
        "BTechStudentDataMEOBCFemale": BTechStudentDataMEOBCFemale,
        "BTechStudentDataMESBCMale": BTechStudentDataMESBCMale,
        "BTechStudentDataMESBCFemale": BTechStudentDataMESBCFemale,
        "BTechStudentDataMECatMFTotal": BTechStudentDataMECatMFTotal,

        "BTechStudentDataELOpenMale": BTechStudentDataELOpenMale,
        "BTechStudentDataELOpenFemale": BTechStudentDataELOpenFemale,
        "BTechStudentDataELSCMale": BTechStudentDataELSCMale,
        "BTechStudentDataELSCFemale": BTechStudentDataELSCFemale,
        "BTechStudentDataELSTMale": BTechStudentDataELSTMale,
        "BTechStudentDataELSTFemale": BTechStudentDataELSTFemale,
        "BTechStudentDataELVJNTMale": BTechStudentDataELVJNTMale,
        "BTechStudentDataELVJNTFemale": BTechStudentDataELVJNTFemale,
        "BTechStudentDataELOBCMale": BTechStudentDataELOBCMale,
        "BTechStudentDataELOBCFemale": BTechStudentDataELOBCFemale,
        "BTechStudentDataELSBCMale": BTechStudentDataELSBCMale,
        "BTechStudentDataELSBCFemale": BTechStudentDataELSBCFemale,
        "BTechStudentDataELCatMFTotal": BTechStudentDataELCatMFTotal,

        "BTechStudentDataETNOpenMale": BTechStudentDataETNOpenMale,
        "BTechStudentDataETNOpenFemale": BTechStudentDataETNOpenFemale,
        "BTechStudentDataETNSCMale": BTechStudentDataETNSCMale,
        "BTechStudentDataETNSCFemale": BTechStudentDataETNSCFemale,
        "BTechStudentDataETNSTMale": BTechStudentDataETNSTMale,
        "BTechStudentDataETNSTFemale": BTechStudentDataETNSTFemale,
        "BTechStudentDataETNVJNTMale": BTechStudentDataETNVJNTMale,
        "BTechStudentDataETNVJNTFemale": BTechStudentDataETNVJNTFemale,
        "BTechStudentDataETNOBCMale": BTechStudentDataETNOBCMale,
        "BTechStudentDataETNOBCFemale": BTechStudentDataETNOBCFemale,
        "BTechStudentDataETNSBCMale": BTechStudentDataETNSBCMale,
        "BTechStudentDataETNSBCFemale": BTechStudentDataETNSBCFemale,
        "BTechStudentDataETNCatMFTotal": BTechStudentDataETNCatMFTotal,

        "BTechStudentDataOpenMaleTotal": BTechStudentDataCSEOpenMale + BTechStudentDataMEOpenMale + BTechStudentDataCVOpenMale + BTechStudentDataITOpenMale + BTechStudentDataELOpenMale + BTechStudentDataETNOpenMale,
        "BTechStudentDataOpenFemaleTotal": BTechStudentDataCSEOpenFemale + BTechStudentDataMEOpenFemale + BTechStudentDataCVOpenFemale + BTechStudentDataITOpenFemale + BTechStudentDataELOpenFemale + BTechStudentDataETNOpenFemale,
        "BTechStudentDataSCMaleTotal": BTechStudentDataCSESCMale + BTechStudentDataMESCMale + BTechStudentDataCVSCMale + BTechStudentDataITSCMale + BTechStudentDataELSCMale + BTechStudentDataETNSCMale,
        "BTechStudentDataSCFemaleTotal": BTechStudentDataCSESCFemale + BTechStudentDataMESCFemale + BTechStudentDataCVSCFemale + BTechStudentDataITSCFemale + BTechStudentDataELSCFemale + BTechStudentDataETNSCFemale,
        "BTechStudentDataSTMaleTotal": BTechStudentDataCSESTMale + BTechStudentDataMESTMale + BTechStudentDataCVSTMale + BTechStudentDataITSTMale + BTechStudentDataELSTMale + BTechStudentDataETNSTMale,
        "BTechStudentDataSTFemaleTotal": BTechStudentDataCSESTFemale + BTechStudentDataMESTFemale + BTechStudentDataCVSTFemale + BTechStudentDataITSTFemale + BTechStudentDataELSTFemale + BTechStudentDataETNSTFemale,
        "BTechStudentDataVJNTMaleTotal": BTechStudentDataCSEVJNTMale + BTechStudentDataMEVJNTMale + BTechStudentDataCVVJNTMale + BTechStudentDataITVJNTMale + BTechStudentDataELVJNTMale + BTechStudentDataETNVJNTMale,
        "BTechStudentDataVJNTFemaleTotal": BTechStudentDataCSEVJNTFemale + BTechStudentDataMEVJNTFemale + BTechStudentDataCVVJNTFemale + BTechStudentDataITVJNTFemale + BTechStudentDataELVJNTFemale + BTechStudentDataETNVJNTFemale,
        "BTechStudentDataOBCMaleTotal": BTechStudentDataCSEOBCMale + BTechStudentDataMEOBCMale + BTechStudentDataCVOBCMale + BTechStudentDataITOBCMale + BTechStudentDataELOBCMale + BTechStudentDataETNOBCMale,
        "BTechStudentDataOBCFemaleTotal": BTechStudentDataCSEOBCFemale + BTechStudentDataMEOBCFemale + BTechStudentDataCVOBCFemale + BTechStudentDataITOBCFemale + BTechStudentDataELOBCFemale + BTechStudentDataETNOBCFemale,
        "BTechStudentDataSBCMaleTotal": BTechStudentDataCSESBCMale + BTechStudentDataMESBCMale + BTechStudentDataCVSBCMale + BTechStudentDataITSBCMale + BTechStudentDataELSBCMale + BTechStudentDataETNSBCMale,
        "BTechStudentDataSBCFemaleTotal": BTechStudentDataCSESBCFemale + BTechStudentDataMESBCFemale + BTechStudentDataCVSBCFemale + BTechStudentDataITSBCFemale + BTechStudentDataELSBCFemale + BTechStudentDataETNSBCFemale,
        "BTechStudentDataFinalCatMFTotal": BTechStudentDataETNCatMFTotal + BTechStudentDataELCatMFTotal + BTechStudentDataMECatMFTotal + BTechStudentDataITCatMFTotal + BTechStudentDataCVCatMFTotal + BTechStudentDataCSECatMFTotal,


        "BTechStudentDataCSEHighestPer": BTechStudentDataCSEHighestPer,
        "BTechStudentDataCVHighestPer": BTechStudentDataCVHighestPer,
        "BTechStudentDataMEHighestPer": BTechStudentDataMEHighestPer,
        "BTechStudentDataITHighestPer": BTechStudentDataITHighestPer,
        "BTechStudentDataELHighestPer": BTechStudentDataELHighestPer,
        "BTechStudentDataETNHighestPer": BTechStudentDataETNHighestPer,

        "BTechStudentDataCSELowestPer": BTechStudentDataCSELowestPer,
        "BTechStudentDataCVLowestPer": BTechStudentDataCVLowestPer,
        "BTechStudentDataITLowestPer": BTechStudentDataITLowestPer,
        "BTechStudentDataMELowestPer": BTechStudentDataMELowestPer,
        "BTechStudentDataELLowestPer": BTechStudentDataELLowestPer,
        "BTechStudentDataETNLowestPer": BTechStudentDataETNLowestPer,

        "BTechStudentDataCSEMale": BTechStudentDataCSEMale,
        "BTechStudentDataCSEFemale": BTechStudentDataCSEFemale,
        "BTechStudentDataCVMale": BTechStudentDataCVMale,
        "BTechStudentDataCVFemale": BTechStudentDataCVFemale,
        "BTechStudentDataITMale": BTechStudentDataITMale,
        "BTechStudentDataITFemale": BTechStudentDataITFemale,
        "BTechStudentDataMEMale": BTechStudentDataMEMale,
        "BTechStudentDataMEFemale": BTechStudentDataMEFemale,
        "BTechStudentDataELMale": BTechStudentDataELMale,
        "BTechStudentDataELFemale": BTechStudentDataELFemale,
        "BTechStudentDataETNMale": BTechStudentDataETNMale,
        "BTechStudentDataETNFemale": BTechStudentDataETNFemale,

        "CSETotalMF": CSETotalMF,
        "CVTotalMF": CVTotalMF,
        "METotalMF": METotalMF,
        "ITTotalMF": ITTotalMF,
        "ELTotalMF": ELTotalMF,
        "ETNTotalMF": ETNTotalMF,

        "TotalM": TotalM,
        "TotalF": TotalF,
        "TotalMF": TotalMF,

        "allResearchPapersCSE": allResearchPapersCSE,
        "countRPCSE": len(allResearchPapersCSE),
        "allResearchPapersCV": allResearchPapersCV,
        "countRPCV": len(allResearchPapersCV),
        "allResearchPapersME": allResearchPapersME,
        "countRPME": len(allResearchPapersME),
        "allResearchPapersIT": allResearchPapersIT,
        "countRPIT": len(allResearchPapersIT),
        "allResearchPapersEL": allResearchPapersEL,
        "countRPEL": len(allResearchPapersEL),
        "allResearchPapersETN": allResearchPapersETN,
        "countRPETN": len(allResearchPapersETN),
        "totalRP": len(allResearchPapersCSE) + len(allResearchPapersCV) + len(allResearchPapersME) + len(allResearchPapersIT) + len(allResearchPapersEL) + len(allResearchPapersETN),

        "allBookPublishedCSE": allBookPublishedCSE,
        "countBookPCSE": len(allBookPublishedCSE),
        "allBookPublishedCV": allBookPublishedCV,
        "countBookPCV": len(allBookPublishedCV),
        "allBookPublishedME": allBookPublishedME,
        "countBookPME": len(allBookPublishedME),
        "allBookPublishedIT": allBookPublishedIT,
        "countBookPIT": len(allBookPublishedIT),
        "allBookPublishedEL": allBookPublishedEL,
        "countBookPEL": len(allBookPublishedEL),
        "allBookPublishedETN": allBookPublishedETN,
        "countBookPETN": len(allBookPublishedETN),
        "totalBookP": len(allBookPublishedCSE) + len(allBookPublishedCV) + len(allBookPublishedME) + len(allBookPublishedIT) + len(allBookPublishedEL) + len(allBookPublishedETN),

        "allPatentsCSE": allPatentsCSE.filter(awarded=True),
        "countPatentsCSE": len(allPatentsCSE),
        "allPatentsCV": allPatentsCV.filter(awarded=True),
        "countPatentsCV": len(allPatentsCV),
        "allPatentsME": allPatentsME.filter(awarded=True),
        "countPatentsME": len(allPatentsME),
        "allPatentsIT": allPatentsIT.filter(awarded=True),
        "countPatentsIT": len(allPatentsIT),
        "allPatentsEL": allPatentsEL.filter(awarded=True),
        "countPatentsEL": len(allPatentsEL),
        "allPatentsETN": allPatentsETN.filter(awarded=True),
        "countPatentsETN": len(allPatentsETN),
        "totalPatents": len(allPatentsCSE) + len(allPatentsCV) + len(allPatentsME) + len(allPatentsIT) + len(allPatentsEL) + len(allPatentsETN),

        "allPatentsNACSE": allPatentsCSE.filter(awarded=False),
        "allPatentsNACV": allPatentsCV.filter(awarded=False),
        "allPatentsNAME": allPatentsME.filter(awarded=False),
        "allPatentsNAIT": allPatentsIT.filter(awarded=False),
        "allPatentsNAEL": allPatentsEL.filter(awarded=False),
        "allPatentsNAETN": allPatentsETN.filter(awarded=False),

        "allCompletedPHDCSE": allCompletedPHDCSE,
        "allCompletedPHDCV": allCompletedPHDCV,
        "allCompletedPHDIT": allCompletedPHDIT,
        "allCompletedPHDME": allCompletedPHDME,
        "allCompletedPHDEL": allCompletedPHDEL,
        "allCompletedPHDETN": allCompletedPHDETN,

        "allOngoingPHDCV": allOngoingPHDCV,
        "allOngoingPHDIT": allOngoingPHDIT,
        "allOngoingPHDCSE": allOngoingPHDCSE,
        "allOngoingPHDME": allOngoingPHDME,
        "allOngoingPHDEL": allOngoingPHDEL,
        "allOngoingPHDETN": allOngoingPHDETN,

        "allFacCompCourseCV": allFacCompCourseCV,
        "allFacCompCourseIT": allFacCompCourseIT,
        "allFacCompCourseCSE": allFacCompCourseCSE,
        "allFacCompCourseME": allFacCompCourseME,
        "allFacCompCourseEL": allFacCompCourseEL,
        "allFacCompCourseETN": allFacCompCourseETN,

        "allPhdStudentOtherCV": allPhdStudentOtherCV,
        "allPhdStudentOtherIT": allPhdStudentOtherIT,
        "allPhdStudentOtherCSE": allPhdStudentOtherCSE,
        "allPhdStudentOtherME": allPhdStudentOtherME,
        "allPhdStudentOtherEL": allPhdStudentOtherEL,
        "allPhdStudentOtherETN": allPhdStudentOtherETN,

        "allPhdStudentQIPCV": allPhdStudentQIPCV,
        "allPhdStudentQIPIT": allPhdStudentQIPIT,
        "allPhdStudentQIPCSE": allPhdStudentQIPCSE,
        "allPhdStudentQIPME": allPhdStudentQIPME,
        "allPhdStudentQIPEL": allPhdStudentQIPEL,
        "allPhdStudentQIPETN": allPhdStudentQIPETN,

        "allPhdStudentNDFCV": allPhdStudentNDFCV,
        "allPhdStudentNDFIT": allPhdStudentNDFIT,
        "allPhdStudentNDFCSE": allPhdStudentNDFCSE,
        "allPhdStudentNDFME": allPhdStudentNDFME,
        "allPhdStudentNDFEL": allPhdStudentNDFEL,
        "allPhdStudentNDFETN": allPhdStudentNDFETN,

        "allGoogleCitationCV": allGoogleCitationCV,
        "allGoogleCitationIT": allGoogleCitationIT,
        "allGoogleCitationCSE": allGoogleCitationCSE,
        "allGoogleCitationME": allGoogleCitationME,
        "allGoogleCitationEL": allGoogleCitationEL,
        "allGoogleCitationETN": allGoogleCitationETN,

        "allGuestLecOrganizedCV": allGuestLecOrganizedCV,
        "allGuestLecOrganizedIT": allGuestLecOrganizedIT,
        "allGuestLecOrganizedCSE": allGuestLecOrganizedCSE,
        "allGuestLecOrganizedME": allGuestLecOrganizedME,
        "allGuestLecOrganizedEL": allGuestLecOrganizedEL,
        "allGuestLecOrganizedETN": allGuestLecOrganizedETN,

        "allGuestLecDeliveredCV": allGuestLecDeliveredCV,
        "allGuestLecDeliveredIT": allGuestLecDeliveredIT,
        "allGuestLecDeliveredCSE": allGuestLecDeliveredCSE,
        "allGuestLecDeliveredME": allGuestLecDeliveredME,
        "allGuestLecDeliveredEL": allGuestLecDeliveredEL,
        "allGuestLecDeliveredETN": allGuestLecDeliveredETN,

        "allEventConductedCV": allEventConductedCV,
        "allEventConductedIT": allEventConductedIT,
        "allEventConductedCSE": allEventConductedCSE,
        "allEventConductedME": allEventConductedME,
        "allEventConductedEL": allEventConductedEL,
        "allEventConductedETN": allEventConductedETN,

        "allEventAttendedCV": allEventAttendedCV,
        "allEventAttendedIT": allEventAttendedIT,
        "allEventAttendedCSE": allEventAttendedCSE,
        "allEventAttendedME": allEventAttendedME,
        "allEventAttendedEL": allEventAttendedEL,
        "allEventAttendedETN": allEventAttendedETN,

        "SerialNoRSPCSE": SerialNoRSPCSE,
        "SerialNoRSPCV": SerialNoRSPCV,
        "SerialNoRSPIT": SerialNoRSPIT,
        "SerialNoRSPME": SerialNoRSPME,
        "SerialNoRSPEL": SerialNoRSPEL,
        "SerialNoRSPETN": SerialNoRSPCSE,

        "SerialNoPHDCSE": SerialNoPHDCSE,
        "SerialNoPHDCV": SerialNoPHDCV,
        "SerialNoPHDIT": SerialNoPHDIT,
        "SerialNoPHDME": SerialNoPHDME,
        "SerialNoPHDEL": SerialNoPHDEL,
        "SerialNoPHDETN": SerialNoPHDETN,

        "SerialNoOngoingPHDCSE": SerialNoOngoingPHDCSE,
        "SerialNoOngoingPHDCV": SerialNoOngoingPHDCV,
        "SerialNoOngoingPHDIT": SerialNoOngoingPHDIT,
        "SerialNoOngoingPHDME": SerialNoOngoingPHDME,
        "SerialNoOngoingPHDEL": SerialNoOngoingPHDEL,
        "SerialNoOngoingPHDETN": SerialNoOngoingPHDETN,

        "SerialNoBookPublishedCSE": SerialNoBookPublishedCSE,
        "SerialNoBookPublishedCV": SerialNoBookPublishedCV,
        "SerialNoBookPublishedIT": SerialNoBookPublishedIT,
        "SerialNoBookPublishedME": SerialNoBookPublishedME,
        "SerialNoBookPublishedEL": SerialNoBookPublishedEL,
        "SerialNoBookPublishedETN": SerialNoBookPublishedETN,

        "SerialNoFacCompCourseCSE": SerialNoFacCompCourseCSE,
        "SerialNoFacCompCourseCV": SerialNoFacCompCourseCV,
        "SerialNoFacCompCourseIT": SerialNoFacCompCourseIT,
        "SerialNoFacCompCourseME": SerialNoFacCompCourseME,
        "SerialNoFacCompCourseEL": SerialNoFacCompCourseEL,
        "SerialNoFacCompCourseETN": SerialNoFacCompCourseETN,

        "SerialNoPhdStudentOtherCSE": SerialNoPhdStudentOtherCSE,
        "SerialNoPhdStudentOtherCV": SerialNoPhdStudentOtherCV,
        "SerialNoPhdStudentOtherIT": SerialNoPhdStudentOtherIT,
        "SerialNoPhdStudentOtherME": SerialNoPhdStudentOtherME,
        "SerialNoPhdStudentOtherEL": SerialNoPhdStudentOtherEL,
        "SerialNoPhdStudentOtherETN": SerialNoPhdStudentOtherETN,

        "SerialNoPhdStudentQIPCSE": SerialNoPhdStudentQIPCSE,
        "SerialNoPhdStudentQIPCV": SerialNoPhdStudentQIPCV,
        "SerialNoPhdStudentQIPIT": SerialNoPhdStudentQIPIT,
        "SerialNoPhdStudentQIPME": SerialNoPhdStudentQIPME,
        "SerialNoPhdStudentQIPEL": SerialNoPhdStudentQIPEL,
        "SerialNoPhdStudentQIPETN": SerialNoPhdStudentQIPETN,

        "SerialNoPhdStudentNDFCSE": SerialNoPhdStudentNDFCSE,
        "SerialNoPhdStudentNDFCV": SerialNoPhdStudentNDFCV,
        "SerialNoPhdStudentNDFIT": SerialNoPhdStudentNDFIT,
        "SerialNoPhdStudentNDFME": SerialNoPhdStudentNDFME,
        "SerialNoPhdStudentNDFEL": SerialNoPhdStudentNDFEL,
        "SerialNoPhdStudentNDFETN": SerialNoPhdStudentNDFETN,

        "isAdmin": isAdmin,
        "fromYear": fromYear,
        "toYear": int(toYear)+1,
    }
    return render(request, "generateReportResult.html", args)


def GeneratePdf(request, fromYear, toYear):
    toYear = int(toYear)-1
    # Student Data

    BTechStudentDataCSEGTE96 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataCSEGTE91To95 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataCSEGTE86To90 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataCSEGTE81To85 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataCSEGTE71To80 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataCSEGTELTE70 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataCSEJKSS = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataCSEJKMigrant = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataCSENEUT = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataCSETotal1 = BTechStudentDataCSEGTE96 + BTechStudentDataCSEGTE91To95 + BTechStudentDataCSEGTE86To90 + BTechStudentDataCSEGTE81To85 + BTechStudentDataCSEGTE71To80 + BTechStudentDataCSEGTELTE70
    BTechStudentDataCSETotal2 = BTechStudentDataCSETotal1 + BTechStudentDataCSEJKSS + BTechStudentDataCSEJKMigrant + BTechStudentDataCSENEUT

    BTechStudentDataCVGTE96 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataCVGTE91To95 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataCVGTE86To90 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataCVGTE81To85 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataCVGTE71To80 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataCVGTELTE70 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataCVJKSS = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataCVJKMigrant = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataCVNEUT = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataCVTotal1 = BTechStudentDataCVGTE96 + BTechStudentDataCVGTE91To95 + BTechStudentDataCVGTE86To90 + BTechStudentDataCVGTE81To85 + BTechStudentDataCVGTE71To80 + BTechStudentDataCVGTELTE70
    BTechStudentDataCVTotal2 = BTechStudentDataCVTotal1 + BTechStudentDataCVJKSS + BTechStudentDataCVJKMigrant + BTechStudentDataCVNEUT

    BTechStudentDataMEGTE96 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataMEGTE91To95 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataMEGTE86To90 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataMEGTE81To85 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataMEGTE71To80 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataMEGTELTE70 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataMEJKSS = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataMEJKMigrant = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataMENEUT = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataMETotal1 = BTechStudentDataMEGTE96 + BTechStudentDataMEGTE91To95 + BTechStudentDataMEGTE86To90 + BTechStudentDataMEGTE81To85 + BTechStudentDataMEGTE71To80 + BTechStudentDataMEGTELTE70
    BTechStudentDataMETotal2 = BTechStudentDataMETotal1 + BTechStudentDataMEJKSS + BTechStudentDataMEJKMigrant + BTechStudentDataMENEUT

    BTechStudentDataITGTE96 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataITGTE91To95 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataITGTE86To90 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataITGTE81To85 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataITGTE71To80 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataITGTELTE70 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataITJKSS = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataITJKMigrant = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataITNEUT = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataITTotal1 = BTechStudentDataITGTE96 + BTechStudentDataITGTE91To95 + BTechStudentDataITGTE86To90 + BTechStudentDataITGTE81To85 + BTechStudentDataITGTE71To80 + BTechStudentDataITGTELTE70
    BTechStudentDataITTotal2 = BTechStudentDataITTotal1 + BTechStudentDataITJKSS + BTechStudentDataITJKMigrant + BTechStudentDataITNEUT

    BTechStudentDataELGTE96 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataELGTE91To95 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataELGTE86To90 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataELGTE81To85 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataELGTE71To80 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataELGTELTE70 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataELJKSS = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataELJKMigrant = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataELNEUT = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataELTotal1 = BTechStudentDataELGTE96 + BTechStudentDataELGTE91To95 + BTechStudentDataELGTE86To90 + BTechStudentDataELGTE81To85 + BTechStudentDataELGTE71To80 + BTechStudentDataELGTELTE70
    BTechStudentDataELTotal2 = BTechStudentDataELTotal1 + BTechStudentDataELJKSS + BTechStudentDataELJKMigrant + BTechStudentDataELNEUT

    BTechStudentDataETNGTE96 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=95.01).count()
    BTechStudentDataETNGTE91To95 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=90.01, CET_Score__lte=95).count()
    BTechStudentDataETNGTE86To90 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=85.01, CET_Score__lte=90).count()
    BTechStudentDataETNGTE81To85 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=80.01, CET_Score__lte=85).count()
    BTechStudentDataETNGTE71To80 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__gte=70.01, CET_Score__lte=80).count()
    BTechStudentDataETNGTELTE70 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(CET_Score__lte=70).count()
    BTechStudentDataETNJKSS = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='PMSSS/JKSSS').count()
    BTechStudentDataETNJKMigrant = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='JK Migrant').count()
    BTechStudentDataETNNEUT = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type='NEUT/GOI').count()
    BTechStudentDataETNTotal1 = BTechStudentDataETNGTE96 + BTechStudentDataETNGTE91To95 + BTechStudentDataETNGTE86To90 + BTechStudentDataETNGTE81To85 + BTechStudentDataETNGTE71To80 + BTechStudentDataETNGTELTE70
    BTechStudentDataETNTotal2 = BTechStudentDataETNTotal1 + BTechStudentDataETNJKSS + BTechStudentDataETNJKMigrant + BTechStudentDataETNNEUT

    # Category Wise Seats List
    BTechStudentDataCSECapSeats = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataCSEWhmtTrust = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataCSEDdTrust = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataCSEEws = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataCSETfws = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataCSEJnK1 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataCSEJnK2 = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataCSENri = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataCSEPmsss = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataCSENeut = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataCSECatTotal = BTechStudentDataCSECapSeats + BTechStudentDataCSEWhmtTrust + BTechStudentDataCSEDdTrust + BTechStudentDataCSEEws + BTechStudentDataCSETfws + BTechStudentDataCSEJnK1 + BTechStudentDataCSEJnK2 + BTechStudentDataCSENri + BTechStudentDataCSEPmsss + BTechStudentDataCSENeut

    BTechStudentDataITCapSeats = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataITWhmtTrust = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataITDdTrust = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataITEws = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataITTfws = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataITJnK1 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataITJnK2 = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataITNri = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataITPmsss = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataITNeut = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataITCatTotal = BTechStudentDataITCapSeats + BTechStudentDataITWhmtTrust + BTechStudentDataITDdTrust + BTechStudentDataITEws + BTechStudentDataITTfws + BTechStudentDataITJnK1 + BTechStudentDataITJnK2 + BTechStudentDataITNri + BTechStudentDataITPmsss + BTechStudentDataITNeut

    BTechStudentDataCVCapSeats = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataCVWhmtTrust = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataCVDdTrust = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataCVEws = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataCVTfws = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataCVJnK1 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataCVJnK2 = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataCVNri = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataCVPmsss = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataCVNeut = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataCVCatTotal = BTechStudentDataCVCapSeats + BTechStudentDataCVWhmtTrust + BTechStudentDataCVDdTrust + BTechStudentDataCVEws + BTechStudentDataCVTfws + BTechStudentDataCVJnK1 + BTechStudentDataCVJnK2 + BTechStudentDataCVNri + BTechStudentDataCVPmsss + BTechStudentDataCVNeut

    BTechStudentDataMECapSeats = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataMEWhmtTrust = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataMEDdTrust = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataMEEws = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataMETfws = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataMEJnK1 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataMEJnK2 = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataMENri = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataMEPmsss = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataMENeut = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataMECatTotal = BTechStudentDataMECapSeats + BTechStudentDataMEWhmtTrust + BTechStudentDataMEDdTrust + BTechStudentDataMEEws + BTechStudentDataMETfws + BTechStudentDataMEJnK1 + BTechStudentDataMEJnK2 + BTechStudentDataMENri + BTechStudentDataMEPmsss + BTechStudentDataMENeut

    BTechStudentDataELCapSeats = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataELWhmtTrust = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataELDdTrust = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataELEws = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataELTfws = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataELJnK1 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataELJnK2 = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataELNri = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataELPmsss = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataELNeut = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataELCatTotal = BTechStudentDataELCapSeats + BTechStudentDataELWhmtTrust + BTechStudentDataELDdTrust + BTechStudentDataELEws + BTechStudentDataELTfws + BTechStudentDataELJnK1 + BTechStudentDataELJnK2 + BTechStudentDataELNri + BTechStudentDataELPmsss + BTechStudentDataELNeut

    BTechStudentDataETNCapSeats = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="Cap Seat").count()
    BTechStudentDataETNWhmtTrust = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="WHMT Trust").count()
    BTechStudentDataETNDdTrust = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="DD Trust").count()
    BTechStudentDataETNEws = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="EWS").count()
    BTechStudentDataETNTfws = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="TFWS").count()
    BTechStudentDataETNJnK1 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K1").count()
    BTechStudentDataETNJnK2 = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="J&K2").count()
    BTechStudentDataETNNri = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NRI/PIO/OCI/CI").count()
    BTechStudentDataETNPmsss = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="PMSSS/JKSSS").count()
    BTechStudentDataETNNeut = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(admission_type="NEUT/GOI").count()
    BTechStudentDataETNCatTotal = BTechStudentDataETNCapSeats + BTechStudentDataETNWhmtTrust + BTechStudentDataETNDdTrust + BTechStudentDataETNEws + BTechStudentDataETNTfws + BTechStudentDataETNJnK1 + BTechStudentDataETNJnK2 + BTechStudentDataETNNri + BTechStudentDataETNPmsss + BTechStudentDataETNNeut

    # Highest %tile Student

    BTechStudentDataCSEHighestPer = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataCSEHighestPer:
        BTechStudentDataCSEHighestPer = BTechStudentDataCSEHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataCSEHighestPer = 0.0

    BTechStudentDataCVHighestPer = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataCVHighestPer:
        BTechStudentDataCVHighestPer = BTechStudentDataCVHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataCVHighestPer = 0.0

    BTechStudentDataMEHighestPer = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataMEHighestPer:
        BTechStudentDataMEHighestPer = BTechStudentDataMEHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataMEHighestPer = 0.0

    BTechStudentDataITHighestPer = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataITHighestPer:
        BTechStudentDataITHighestPer = BTechStudentDataITHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataITHighestPer = 0.0

    BTechStudentDataELHighestPer = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataELHighestPer:
        BTechStudentDataELHighestPer = BTechStudentDataELHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataELHighestPer = 0.0

    BTechStudentDataETNHighestPer = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataETNHighestPer:
        BTechStudentDataETNHighestPer = BTechStudentDataETNHighestPer.latest('CET_Score').CET_Score
    else:
        BTechStudentDataETNHighestPer = 0.0

    # Lowest %tile Student

    BTechStudentDataCSELowestPer = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataCSEHighestPer:
        ab = []
        for i in BTechStudentDataCSELowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataCSELowestPer = res_min
    else:
        BTechStudentDataCSELowestPer = 0.0

    BTechStudentDataCVLowestPer = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataCVHighestPer:
        ab = []
        for i in BTechStudentDataCVLowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataCVLowestPer = res_min
    else:
        BTechStudentDataCVLowestPer = 0.0

    BTechStudentDataMELowestPer = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataMEHighestPer:
        ab = []
        for i in BTechStudentDataMELowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataMELowestPer = res_min
    else:
        BTechStudentDataMELowestPer = 0.0

    BTechStudentDataITLowestPer = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataITHighestPer:
        ab = []
        for i in BTechStudentDataITLowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataITLowestPer = res_min
    else:
        BTechStudentDataITLowestPer = 0.0

    BTechStudentDataELLowestPer = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataELHighestPer:
        ab = []
        for i in BTechStudentDataELLowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataELLowestPer = res_min
    else:
        BTechStudentDataELLowestPer = 0.0

    BTechStudentDataETNLowestPer = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    if BTechStudentDataETNHighestPer:
        ab = []
        for i in BTechStudentDataETNLowestPer:
            ab.append(i.CET_Score)
        res_min = min(ab, key=lambda x: float(x))
        BTechStudentDataETNLowestPer = res_min
    else:
        BTechStudentDataETNLowestPer = 0.0

    # Student Gender
    BTechStudentDataCSEMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataCSEFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataCVMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataCVFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataMEMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataMEFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataITMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataITFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataELMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataELFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    BTechStudentDataETNMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Male').count()
    BTechStudentDataETNFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(gender='Female').count()

    CSETotalMF = BTechStudentDataCSEMale + BTechStudentDataCSEFemale
    CVTotalMF = BTechStudentDataCVMale + BTechStudentDataCVFemale
    ELTotalMF = BTechStudentDataELMale + BTechStudentDataELFemale
    ITTotalMF = BTechStudentDataITMale + BTechStudentDataITFemale
    METotalMF = BTechStudentDataMEMale + BTechStudentDataMEFemale
    ETNTotalMF = BTechStudentDataETNMale + BTechStudentDataETNFemale

    TotalM = BTechStudentDataCSEMale + BTechStudentDataCVMale + BTechStudentDataELMale + BTechStudentDataITMale + BTechStudentDataMEMale + BTechStudentDataETNMale
    TotalF = BTechStudentDataCSEFemale + BTechStudentDataCVFemale + BTechStudentDataELFemale + BTechStudentDataITFemale + BTechStudentDataMEFemale + BTechStudentDataETNFemale

    TotalMF = CSETotalMF + CVTotalMF + ELTotalMF + ITTotalMF + METotalMF + ETNTotalMF

    # Number of Students from Reservation Categories
    BTechStudentDataCSEOpenMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataCSEOpenFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataCSESCMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataCSESCFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataCSESTMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataCSESTFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataCSEVJNTMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataCSEVJNTFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataCSEOBCMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataCSEOBCFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataCSESBCMale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataCSESBCFemale = BTechStudentDataCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataCSECatMFTotal = BTechStudentDataCSEOpenMale + BTechStudentDataCSEOpenFemale + BTechStudentDataCSESCMale + BTechStudentDataCSESCFemale + BTechStudentDataCSESTMale + BTechStudentDataCSESTFemale + BTechStudentDataCSEVJNTMale + BTechStudentDataCSEVJNTFemale + BTechStudentDataCSEOBCMale + BTechStudentDataCSEOBCFemale + BTechStudentDataCSESBCMale + BTechStudentDataCSESBCFemale

    BTechStudentDataITOpenMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataITOpenFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataITSCMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataITSCFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataITSTMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataITSTFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataITVJNTMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataITVJNTFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataITOBCMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataITOBCFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataITSBCMale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataITSBCFemale = BTechStudentDataIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataITCatMFTotal = BTechStudentDataITOpenMale + BTechStudentDataITOpenFemale + BTechStudentDataITSCMale + BTechStudentDataITSCFemale + BTechStudentDataITSTMale + BTechStudentDataITSTFemale + BTechStudentDataITVJNTMale + BTechStudentDataITVJNTFemale + BTechStudentDataITOBCMale + BTechStudentDataITOBCFemale + BTechStudentDataITSBCMale + BTechStudentDataITSBCFemale

    BTechStudentDataCVOpenMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataCVOpenFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataCVSCMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataCVSCFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataCVSTMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataCVSTFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataCVVJNTMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataCVVJNTFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataCVOBCMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataCVOBCFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataCVSBCMale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataCVSBCFemale = BTechStudentDataCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataCVCatMFTotal = BTechStudentDataCVOpenMale + BTechStudentDataCVOpenFemale + BTechStudentDataCVSCMale + BTechStudentDataCVSCFemale + BTechStudentDataCVSTMale + BTechStudentDataCVSTFemale + BTechStudentDataCVVJNTMale + BTechStudentDataCVVJNTFemale + BTechStudentDataCVOBCMale + BTechStudentDataCVOBCFemale + BTechStudentDataCVSBCMale + BTechStudentDataCVSBCFemale

    BTechStudentDataMEOpenMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataMEOpenFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataMESCMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataMESCFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataMESTMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataMESTFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataMEVJNTMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataMEVJNTFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataMEOBCMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataMEOBCFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataMESBCMale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataMESBCFemale = BTechStudentDataME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataMECatMFTotal = BTechStudentDataMEOpenMale + BTechStudentDataMEOpenFemale + BTechStudentDataMESCMale + BTechStudentDataMESCFemale + BTechStudentDataMESTMale + BTechStudentDataMESTFemale + BTechStudentDataMEVJNTMale + BTechStudentDataMEVJNTFemale + BTechStudentDataMEOBCMale + BTechStudentDataMEOBCFemale + BTechStudentDataMESBCMale + BTechStudentDataMESBCFemale

    BTechStudentDataELOpenMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataELOpenFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataELSCMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataELSCFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataELSTMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataELSTFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataELVJNTMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataELVJNTFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataELOBCMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataELOBCFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataELSBCMale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataELSBCFemale = BTechStudentDataEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataELCatMFTotal = BTechStudentDataELOpenMale + BTechStudentDataELOpenFemale + BTechStudentDataELSCMale + BTechStudentDataELSCFemale + BTechStudentDataELSTMale + BTechStudentDataELSTFemale + BTechStudentDataELVJNTMale + BTechStudentDataELVJNTFemale + BTechStudentDataELOBCMale + BTechStudentDataELOBCFemale + BTechStudentDataELSBCMale + BTechStudentDataELSBCFemale

    BTechStudentDataETNOpenMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Male').count()
    BTechStudentDataETNOpenFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="General").filter(gender='Female').count()
    BTechStudentDataETNSCMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Male').count()
    BTechStudentDataETNSCFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Caste(SC)").filter(gender='Female').count()
    BTechStudentDataETNSTMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Male').count()
    BTechStudentDataETNSTFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Scheduled Tribes(ST)").filter(gender='Female').count()
    BTechStudentDataETNVJNTMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Male').count()
    BTechStudentDataETNVJNTFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Vimukta Jat Nomadic Tribes(VJNT)").filter(gender='Female').count()
    BTechStudentDataETNOBCMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Male').count()
    BTechStudentDataETNOBCFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Other Backward Class(OBC)").filter(gender='Female').count()
    BTechStudentDataETNSBCMale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Male').count()
    BTechStudentDataETNSBCFemale = BTechStudentDataETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(category="Special Backward Class(SBC)").filter(gender='Female').count()
    BTechStudentDataETNCatMFTotal = BTechStudentDataETNOpenMale + BTechStudentDataETNOpenFemale + BTechStudentDataETNSCMale + BTechStudentDataETNSCFemale + BTechStudentDataETNSTMale + BTechStudentDataETNSTFemale + BTechStudentDataETNVJNTMale + BTechStudentDataETNVJNTFemale + BTechStudentDataETNOBCMale + BTechStudentDataETNOBCFemale + BTechStudentDataETNSBCMale + BTechStudentDataETNSBCFemale

    # Research Paper
    allResearchPapersCSE = ResearchPaperCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersCV = ResearchPaperCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersME = ResearchPaperME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersIT = ResearchPaperIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersEL = ResearchPaperEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allResearchPapersETN = ResearchPaperETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)

    # Book Published
    allBookPublishedCSE = BookPublishedCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedCV = BookPublishedCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedME = BookPublishedME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedIT = BookPublishedIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedEL = BookPublishedEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allBookPublishedETN = BookPublishedETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)

    # Patents
    allPatentsCSE = PatentsCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsCV = PatentsCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsME = PatentsME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsIT = PatentsIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsEL = PatentsEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allPatentsETN = PatentETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)

    # PHD Details - Completed
    allCompletedPHDCSE = PhdCSE.objects.filter(status=True)
    allCompletedPHDIT = PhdIT.objects.filter(status=True)
    allCompletedPHDCV = PhdCV.objects.filter(status=True)
    allCompletedPHDME = PhdME.objects.filter(status=True)
    allCompletedPHDEL = PhdEL.objects.filter(status=True)
    allCompletedPHDETN = PhdETN.objects.filter(status=True)

    # PHD Details - Ongoing
    allOngoingPHDCSE = PhdCSE.objects.filter(status=False)
    allOngoingPHDME = PhdME.objects.filter(status=False)
    allOngoingPHDCV = PhdCV.objects.filter(status=False)
    allOngoingPHDIT = PhdIT.objects.filter(status=False)
    allOngoingPHDEL = PhdEL.objects.filter(status=False)
    allOngoingPHDETN = PhdETN.objects.filter(status=False)

    # Faculty Completed Courses
    allFacCompCourseCSE = FacultyCompletedCourseCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseME = FacultyCompletedCourseME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseCV = FacultyCompletedCourseCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseIT = FacultyCompletedCourseIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseEL = FacultyCompletedCourseEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")
    allFacCompCourseETN = FacultyCompletedCourseETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).order_by("faculty_name")

    # Ph.D.Student Details registered under WCE faculty(other than QIP - Ph.D. and NDF students)
    allPhdStudentOtherCSE = GuideforPHDCSE.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherME = GuideforPHDME.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherIT = GuideforPHDIT.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherCV = GuideforPHDCV.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherEL = GuideforPHDEL.objects.filter(type_of_phd="Other").order_by("guide_name")
    allPhdStudentOtherETN = GuideforPHDETN.objects.filter(type_of_phd="Other").order_by("guide_name")

    # Ph.D.Student Details registered under WCE faculty(QIP - Ph.D. students)
    allPhdStudentQIPCSE = GuideforPHDCSE.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPME = GuideforPHDME.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPIT = GuideforPHDIT.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPCV = GuideforPHDCV.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPEL = GuideforPHDEL.objects.filter(type_of_phd="QIP").order_by("guide_name")
    allPhdStudentQIPETN = GuideforPHDETN.objects.filter(type_of_phd="QIP").order_by("guide_name")

    # Ph.D.Student Details registered under WCE faculty(NDF Ph.D. students)
    allPhdStudentNDFCSE = GuideforPHDCSE.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFME = GuideforPHDME.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFIT = GuideforPHDIT.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFCV = GuideforPHDCV.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFEL = GuideforPHDEL.objects.filter(type_of_phd="NDF").order_by("guide_name")
    allPhdStudentNDFETN = GuideforPHDETN.objects.filter(type_of_phd="NDF").order_by("guide_name")

    # Google Scholar Citation Details
    allGoogleCitationCSE = GoogleScholarCitationDetailsCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationIT = GoogleScholarCitationDetailsIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationCV = GoogleScholarCitationDetailsCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationME = GoogleScholarCitationDetailsME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationEL = GoogleScholarCitationDetailsEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)
    allGoogleCitationETN = GoogleScholarCitationDetailsETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear)

    # Guest Lecture Organized by Faculty
    allGuestLecOrganizedCSE = GuestLecOrganizedOrDeliveredCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedIT = GuestLecOrganizedOrDeliveredIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedME = GuestLecOrganizedOrDeliveredME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedCV = GuestLecOrganizedOrDeliveredCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedEL = GuestLecOrganizedOrDeliveredEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")
    allGuestLecOrganizedETN = GuestLecOrganizedOrDeliveredETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Organized").order_by("teacher_name")

    # Guest Lecture Delivered by Faculty
    allGuestLecDeliveredCSE = GuestLecOrganizedOrDeliveredCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredIT = GuestLecOrganizedOrDeliveredIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredME = GuestLecOrganizedOrDeliveredME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredCV = GuestLecOrganizedOrDeliveredCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredEL = GuestLecOrganizedOrDeliveredEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")
    allGuestLecDeliveredETN = GuestLecOrganizedOrDeliveredETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type="Delivered").order_by("teacher_name")

    # Activities Conducted
    allEventConductedCSE = EventConductedOrAttendedCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedIT = EventConductedOrAttendedIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedME = EventConductedOrAttendedME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedCV = EventConductedOrAttendedCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedEL = EventConductedOrAttendedEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")
    allEventConductedETN = EventConductedOrAttendedETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Conducted").order_by("teacher_name")

    # Events Attended by Faculty
    allEventAttendedCSE = EventConductedOrAttendedCSE.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedIT = EventConductedOrAttendedIT.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedME = EventConductedOrAttendedME.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedCV = EventConductedOrAttendedCV.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedEL = EventConductedOrAttendedEL.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")
    allEventAttendedETN = EventConductedOrAttendedETN.objects.filter(academic_year__gte=fromYear, academic_year__lte=toYear).filter(type_of_event="Attended").order_by("teacher_name")

    # For Displaying Serial No Research Paper
    SerialNoRSPCSE = []
    for i in range(len(allResearchPapersCSE)):
        SerialNoRSPCSE.insert(i, i+1)
    SerialNoRSPIT = []
    for i in range(len(allResearchPapersIT)):
        SerialNoRSPIT.insert(i, i+1)
    SerialNoRSPME = []
    for i in range(len(allResearchPapersME)):
        SerialNoRSPME.insert(i, i+1)
    SerialNoRSPCV = []
    for i in range(len(allResearchPapersCV)):
        SerialNoRSPCV.insert(i, i+1)
    SerialNoRSPEL = []
    for i in range(len(allResearchPapersEL)):
        SerialNoRSPEL.insert(i, i+1)
    SerialNoRSPETN = []
    for i in range(len(allResearchPapersETN)):
        SerialNoRSPETN.insert(i, i+1)

    # For Displaying Serial No Completed PHD
    SerialNoPHDETN = []
    for i in range(len(allCompletedPHDETN)):
        SerialNoPHDETN.insert(i, i + 1)
    c = len(allCompletedPHDETN) + len(allCompletedPHDCV)
    SerialNoPHDCV = []
    for i in range(len(allCompletedPHDETN), c):
        SerialNoPHDCV.insert(i, i + 1)
    SerialNoPHDME = []
    for i in range(c, len(allCompletedPHDME)+c):
        SerialNoPHDME.insert(i, i + 1)
    c += len(allCompletedPHDME)
    SerialNoPHDEL = []
    for i in range(c, len(allCompletedPHDEL)+c):
        SerialNoPHDEL.insert(i, i + 1)
    c += len(allCompletedPHDEL)
    SerialNoPHDIT = []
    for i in range(c, len(allCompletedPHDIT)+c):
        SerialNoPHDIT.insert(i, i + 1)
    c += len(allCompletedPHDIT)
    SerialNoPHDCSE = []
    for i in range(c, len(allCompletedPHDCSE)+c):
        SerialNoPHDCSE.insert(i, i + 1)

    # For Displaying Serial No Ongoing PHD
    SerialNoOngoingPHDETN = []
    for i in range(len(allOngoingPHDETN)):
        SerialNoOngoingPHDETN.insert(i, i + 1)
    c = len(allOngoingPHDETN) + len(allOngoingPHDCV)
    SerialNoOngoingPHDCV = []
    for i in range(len(allOngoingPHDETN), c):
        SerialNoOngoingPHDCV.insert(i, i + 1)
    SerialNoOngoingPHDME = []
    for i in range(c, len(allOngoingPHDME) + c):
        SerialNoOngoingPHDME.insert(i, i + 1)
    c += len(allOngoingPHDME)
    SerialNoOngoingPHDEL = []
    for i in range(c, len(allOngoingPHDEL) + c):
        SerialNoOngoingPHDEL.insert(i, i + 1)
    c += len(allOngoingPHDEL)
    SerialNoOngoingPHDIT = []
    for i in range(c, len(allOngoingPHDIT) + c):
        SerialNoOngoingPHDIT.insert(i, i + 1)
    c += len(allOngoingPHDIT)
    SerialNoOngoingPHDCSE = []
    for i in range(c, len(allOngoingPHDCSE) + c):
        SerialNoOngoingPHDCSE.insert(i, i + 1)

    # For Displaying Serial No Book Published
    SerialNoBookPublishedETN = []
    for i in range(len(allBookPublishedETN)):
        SerialNoBookPublishedETN.insert(i, i + 1)
    c = len(allBookPublishedETN) + len(allBookPublishedCV)
    SerialNoBookPublishedCV = []
    for i in range(len(allBookPublishedETN), c):
        SerialNoBookPublishedCV.insert(i, i + 1)
    SerialNoBookPublishedME = []
    for i in range(c, len(allBookPublishedME) + c):
        SerialNoBookPublishedME.insert(i, i + 1)
    c += len(allBookPublishedME)
    SerialNoBookPublishedEL = []
    for i in range(c, len(allBookPublishedEL) + c):
        SerialNoBookPublishedEL.insert(i, i + 1)
    c += len(allBookPublishedEL)
    SerialNoBookPublishedIT = []
    for i in range(c, len(allBookPublishedIT) + c):
        SerialNoBookPublishedIT.insert(i, i + 1)
    c += len(allBookPublishedIT)
    SerialNoBookPublishedCSE = []
    for i in range(c, len(allBookPublishedCSE) + c):
        SerialNoBookPublishedCSE.insert(i, i + 1)

    # For Displaying Serial No Faculty Completed Courses
    SerialNoFacCompCourseETN = []
    for i in range(len(allFacCompCourseETN)):
        SerialNoFacCompCourseETN.insert(i, i + 1)
    c = len(allFacCompCourseETN) + len(allFacCompCourseCV)
    SerialNoFacCompCourseCV = []
    for i in range(len(allFacCompCourseETN), c):
        SerialNoFacCompCourseCV.insert(i, i + 1)
    SerialNoFacCompCourseME = []
    for i in range(c, len(allFacCompCourseME) + c):
        SerialNoFacCompCourseME.insert(i, i + 1)
    c += len(allFacCompCourseME)
    SerialNoFacCompCourseEL = []
    for i in range(c, len(allFacCompCourseEL) + c):
        SerialNoFacCompCourseEL.insert(i, i + 1)
    c += len(allFacCompCourseEL)
    SerialNoFacCompCourseIT = []
    for i in range(c, len(allFacCompCourseIT) + c):
        SerialNoFacCompCourseIT.insert(i, i + 1)
    c += len(allFacCompCourseIT)
    SerialNoFacCompCourseCSE = []
    for i in range(c, len(allFacCompCourseCSE) + c):
        SerialNoFacCompCourseCSE.insert(i, i + 1)

    # For Displaying Serial No Ph.D.Student Details registered under WCE faculty(other than QIP - Ph.D. and NDF students)
    SerialNoPhdStudentOtherETN = []
    for i in range(len(allPhdStudentOtherETN)):
        SerialNoPhdStudentOtherETN.insert(i, i + 1)
    c = len(allPhdStudentOtherETN) + len(allPhdStudentOtherCV)
    SerialNoPhdStudentOtherCV = []
    for i in range(len(allPhdStudentOtherETN), c):
        SerialNoPhdStudentOtherCV.insert(i, i + 1)
    SerialNoPhdStudentOtherME = []
    for i in range(c, len(allPhdStudentOtherME) + c):
        SerialNoPhdStudentOtherME.insert(i, i + 1)
    c += len(allPhdStudentOtherME)
    SerialNoPhdStudentOtherEL = []
    for i in range(c, len(allPhdStudentOtherEL) + c):
        SerialNoPhdStudentOtherEL.insert(i, i + 1)
    c += len(allPhdStudentOtherEL)
    SerialNoPhdStudentOtherIT = []
    for i in range(c, len(allPhdStudentOtherIT) + c):
        SerialNoPhdStudentOtherIT.insert(i, i + 1)
    c += len(allPhdStudentOtherIT)
    SerialNoPhdStudentOtherCSE = []
    for i in range(c, len(allPhdStudentOtherCSE) + c):
        SerialNoPhdStudentOtherCSE.insert(i, i + 1)

    # For Displaying Serial No Ph.D.Student Details registered under WCE faculty(QIP - Ph.D. students)
    SerialNoPhdStudentQIPETN = []
    for i in range(len(allPhdStudentQIPETN)):
        SerialNoPhdStudentQIPETN.insert(i, i + 1)
    c = len(allPhdStudentQIPETN) + len(allPhdStudentQIPCV)
    SerialNoPhdStudentQIPCV = []
    for i in range(len(allPhdStudentQIPETN), c):
        SerialNoPhdStudentQIPCV.insert(i, i + 1)
    SerialNoPhdStudentQIPME = []
    for i in range(c, len(allPhdStudentQIPME) + c):
        SerialNoPhdStudentQIPME.insert(i, i + 1)
    c += len(allPhdStudentQIPME)
    SerialNoPhdStudentQIPEL = []
    for i in range(c, len(allPhdStudentQIPEL) + c):
        SerialNoPhdStudentQIPEL.insert(i, i + 1)
    c += len(allPhdStudentQIPEL)
    SerialNoPhdStudentQIPIT = []
    for i in range(c, len(allPhdStudentQIPIT) + c):
        SerialNoPhdStudentQIPIT.insert(i, i + 1)
    c += len(allPhdStudentQIPIT)
    SerialNoPhdStudentQIPCSE = []
    for i in range(c, len(allPhdStudentQIPCSE) + c):
        SerialNoPhdStudentQIPCSE.insert(i, i + 1)

    # For Displaying Serial No Ph.D.Student Details registered under WCE faculty(NDF Ph.D. students)
    SerialNoPhdStudentNDFETN = []
    for i in range(len(allPhdStudentNDFETN)):
        SerialNoPhdStudentNDFETN.insert(i, i + 1)
    c = len(allPhdStudentNDFETN) + len(allPhdStudentNDFCV)
    SerialNoPhdStudentNDFCV = []
    for i in range(len(allPhdStudentNDFETN), c):
        SerialNoPhdStudentNDFCV.insert(i, i + 1)
    SerialNoPhdStudentNDFME = []
    for i in range(c, len(allPhdStudentNDFME) + c):
        SerialNoPhdStudentNDFME.insert(i, i + 1)
    c += len(allPhdStudentNDFME)
    SerialNoPhdStudentNDFEL = []
    for i in range(c, len(allPhdStudentNDFEL) + c):
        SerialNoPhdStudentNDFEL.insert(i, i + 1)
    c += len(allPhdStudentNDFEL)
    SerialNoPhdStudentNDFIT = []
    for i in range(c, len(allPhdStudentNDFIT) + c):
        SerialNoPhdStudentNDFIT.insert(i, i + 1)
    c += len(allPhdStudentNDFIT)
    SerialNoPhdStudentNDFCSE = []
    for i in range(c, len(allPhdStudentNDFCSE) + c):
        SerialNoPhdStudentNDFCSE.insert(i, i + 1)


    # Passing args to template for displaying data
    args = {
        "BTechStudentDataCSEGTE96": BTechStudentDataCSEGTE96,
        "BTechStudentDataCSEGTE91To95": BTechStudentDataCSEGTE91To95,
        "BTechStudentDataCSEGTE86To90": BTechStudentDataCSEGTE86To90,
        "BTechStudentDataCSEGTE81To85": BTechStudentDataCSEGTE81To85,
        "BTechStudentDataCSEGTE71To80": BTechStudentDataCSEGTE71To80,
        "BTechStudentDataCSEGTELTE70": BTechStudentDataCSEGTELTE70,
        "BTechStudentDataCSEJKSS": BTechStudentDataCSEJKSS,
        "BTechStudentDataCSEJKMigrant": BTechStudentDataCSEJKMigrant,
        "BTechStudentDataCSENEUT": BTechStudentDataCSENEUT,
        "BTechStudentDataCSETotal1": BTechStudentDataCSETotal1,
        "BTechStudentDataCSETotal2": BTechStudentDataCSETotal2,

        "BTechStudentDataCVGTE96": BTechStudentDataCVGTE96,
        "BTechStudentDataCVGTE91To95": BTechStudentDataCVGTE91To95,
        "BTechStudentDataCVGTE86To90": BTechStudentDataCVGTE86To90,
        "BTechStudentDataCVGTE81To85": BTechStudentDataCVGTE81To85,
        "BTechStudentDataCVGTE71To80": BTechStudentDataCVGTE71To80,
        "BTechStudentDataCVGTELTE70": BTechStudentDataCVGTELTE70,
        "BTechStudentDataCVJKSS": BTechStudentDataCVJKSS,
        "BTechStudentDataCVJKMigrant": BTechStudentDataCVJKMigrant,
        "BTechStudentDataCVNEUT": BTechStudentDataCVNEUT,
        "BTechStudentDataCVTotal1": BTechStudentDataCVTotal1,
        "BTechStudentDataCVTotal2": BTechStudentDataCVTotal2,

        "BTechStudentDataITGTE96": BTechStudentDataITGTE96,
        "BTechStudentDataITGTE91To95": BTechStudentDataITGTE91To95,
        "BTechStudentDataITGTE86To90": BTechStudentDataITGTE86To90,
        "BTechStudentDataITGTE81To85": BTechStudentDataITGTE81To85,
        "BTechStudentDataITGTE71To80": BTechStudentDataITGTE71To80,
        "BTechStudentDataITGTELTE70": BTechStudentDataITGTELTE70,
        "BTechStudentDataITJKSS": BTechStudentDataITJKSS,
        "BTechStudentDataITJKMigrant": BTechStudentDataITJKMigrant,
        "BTechStudentDataITNEUT": BTechStudentDataITNEUT,
        "BTechStudentDataITTotal1": BTechStudentDataITTotal1,
        "BTechStudentDataITTotal2": BTechStudentDataITTotal2,

        "BTechStudentDataMEGTE96": BTechStudentDataMEGTE96,
        "BTechStudentDataMEGTE91To95": BTechStudentDataMEGTE91To95,
        "BTechStudentDataMEGTE86To90": BTechStudentDataMEGTE86To90,
        "BTechStudentDataMEGTE81To85": BTechStudentDataMEGTE81To85,
        "BTechStudentDataMEGTE71To80": BTechStudentDataMEGTE71To80,
        "BTechStudentDataMEGTELTE70": BTechStudentDataMEGTELTE70,
        "BTechStudentDataMEJKSS": BTechStudentDataMEJKSS,
        "BTechStudentDataMEJKMigrant": BTechStudentDataMEJKMigrant,
        "BTechStudentDataMENEUT": BTechStudentDataMENEUT,
        "BTechStudentDataMETotal1": BTechStudentDataMETotal1,
        "BTechStudentDataMETotal2": BTechStudentDataMETotal2,

        "BTechStudentDataELGTE96": BTechStudentDataELGTE96,
        "BTechStudentDataELGTE91To95": BTechStudentDataELGTE91To95,
        "BTechStudentDataELGTE86To90": BTechStudentDataELGTE86To90,
        "BTechStudentDataELGTE81To85": BTechStudentDataELGTE81To85,
        "BTechStudentDataELGTE71To80": BTechStudentDataELGTE71To80,
        "BTechStudentDataELGTELTE70": BTechStudentDataELGTELTE70,
        "BTechStudentDataELJKSS": BTechStudentDataELJKSS,
        "BTechStudentDataELJKMigrant": BTechStudentDataELJKMigrant,
        "BTechStudentDataELNEUT": BTechStudentDataELNEUT,
        "BTechStudentDataELTotal1": BTechStudentDataELTotal1,
        "BTechStudentDataELTotal2": BTechStudentDataELTotal2,

        "BTechStudentDataETNGTE96": BTechStudentDataETNGTE96,
        "BTechStudentDataETNGTE91To95": BTechStudentDataETNGTE91To95,
        "BTechStudentDataETNGTE86To90": BTechStudentDataETNGTE86To90,
        "BTechStudentDataETNGTE81To85": BTechStudentDataETNGTE81To85,
        "BTechStudentDataETNGTE71To80": BTechStudentDataETNGTE71To80,
        "BTechStudentDataETNGTELTE70": BTechStudentDataETNGTELTE70,
        "BTechStudentDataETNJKSS": BTechStudentDataETNJKSS,
        "BTechStudentDataETNJKMigrant": BTechStudentDataETNJKMigrant,
        "BTechStudentDataETNNEUT": BTechStudentDataETNNEUT,
        "BTechStudentDataETNTotal1": BTechStudentDataETNTotal1,
        "BTechStudentDataETNTotal2": BTechStudentDataETNTotal2,

        "BTechStudentDataCSECapSeats": BTechStudentDataCSECapSeats,
        "BTechStudentDataCSEWhmtTrust": BTechStudentDataCSEWhmtTrust,
        "BTechStudentDataCSEDdTrust": BTechStudentDataCSEDdTrust,
        "BTechStudentDataCSEEws": BTechStudentDataCSEEws,
        "BTechStudentDataCSETfws": BTechStudentDataCSETfws,
        "BTechStudentDataCSEJnK1": BTechStudentDataCSEJnK1,
        "BTechStudentDataCSEJnK2": BTechStudentDataCSEJnK2,
        "BTechStudentDataCSENri": BTechStudentDataCSENri,
        "BTechStudentDataCSEPmsss": BTechStudentDataCSEPmsss,
        "BTechStudentDataCSENeut": BTechStudentDataCSENeut,
        "BTechStudentDataCSECatTotal": BTechStudentDataCSECatTotal,

        "BTechStudentDataCVCapSeats": BTechStudentDataCVCapSeats,
        "BTechStudentDataCVWhmtTrust": BTechStudentDataCVWhmtTrust,
        "BTechStudentDataCVDdTrust": BTechStudentDataCVDdTrust,
        "BTechStudentDataCVEws": BTechStudentDataCVEws,
        "BTechStudentDataCVTfws": BTechStudentDataCVTfws,
        "BTechStudentDataCVJnK1": BTechStudentDataCVJnK1,
        "BTechStudentDataCVJnK2": BTechStudentDataCVJnK2,
        "BTechStudentDataCVNri": BTechStudentDataCVNri,
        "BTechStudentDataCVPmsss": BTechStudentDataCVPmsss,
        "BTechStudentDataCVNeut": BTechStudentDataCVNeut,
        "BTechStudentDataCVCatTotal": BTechStudentDataCVCatTotal,

        "BTechStudentDataITCapSeats": BTechStudentDataITCapSeats,
        "BTechStudentDataITWhmtTrust": BTechStudentDataITWhmtTrust,
        "BTechStudentDataITDdTrust": BTechStudentDataITDdTrust,
        "BTechStudentDataITEws": BTechStudentDataITEws,
        "BTechStudentDataITTfws": BTechStudentDataITTfws,
        "BTechStudentDataITJnK1": BTechStudentDataITJnK1,
        "BTechStudentDataITJnK2": BTechStudentDataITJnK2,
        "BTechStudentDataITNri": BTechStudentDataITNri,
        "BTechStudentDataITPmsss": BTechStudentDataITPmsss,
        "BTechStudentDataITNeut": BTechStudentDataITNeut,
        "BTechStudentDataITCatTotal": BTechStudentDataITCatTotal,

        "BTechStudentDataMECapSeats": BTechStudentDataMECapSeats,
        "BTechStudentDataMEWhmtTrust": BTechStudentDataMEWhmtTrust,
        "BTechStudentDataMEDdTrust": BTechStudentDataMEDdTrust,
        "BTechStudentDataMEEws": BTechStudentDataMEEws,
        "BTechStudentDataMETfws": BTechStudentDataMETfws,
        "BTechStudentDataMEJnK1": BTechStudentDataMEJnK1,
        "BTechStudentDataMEJnK2": BTechStudentDataMEJnK2,
        "BTechStudentDataMENri": BTechStudentDataMENri,
        "BTechStudentDataMEPmsss": BTechStudentDataMEPmsss,
        "BTechStudentDataMENeut": BTechStudentDataMENeut,
        "BTechStudentDataMECatTotal": BTechStudentDataMECatTotal,

        "BTechStudentDataELCapSeats": BTechStudentDataELCapSeats,
        "BTechStudentDataELWhmtTrust": BTechStudentDataELWhmtTrust,
        "BTechStudentDataELDdTrust": BTechStudentDataELDdTrust,
        "BTechStudentDataELEws": BTechStudentDataELEws,
        "BTechStudentDataELTfws": BTechStudentDataELTfws,
        "BTechStudentDataELJnK1": BTechStudentDataELJnK1,
        "BTechStudentDataELJnK2": BTechStudentDataELJnK2,
        "BTechStudentDataELNri": BTechStudentDataELNri,
        "BTechStudentDataELPmsss": BTechStudentDataELPmsss,
        "BTechStudentDataELNeut": BTechStudentDataELNeut,
        "BTechStudentDataELCatTotal": BTechStudentDataELCatTotal,

        "BTechStudentDataETNCapSeats": BTechStudentDataETNCapSeats,
        "BTechStudentDataETNWhmtTrust": BTechStudentDataETNWhmtTrust,
        "BTechStudentDataETNDdTrust": BTechStudentDataETNDdTrust,
        "BTechStudentDataETNEws": BTechStudentDataETNEws,
        "BTechStudentDataETNTfws": BTechStudentDataETNTfws,
        "BTechStudentDataETNJnK1": BTechStudentDataETNJnK1,
        "BTechStudentDataETNJnK2": BTechStudentDataETNJnK2,
        "BTechStudentDataETNNri": BTechStudentDataETNNri,
        "BTechStudentDataETNPmsss": BTechStudentDataETNPmsss,
        "BTechStudentDataETNNeut": BTechStudentDataETNNeut,
        "BTechStudentDataETNCatTotal": BTechStudentDataETNCatTotal,

        "BTechStudentDataTotalCapSeats": BTechStudentDataCVCapSeats + BTechStudentDataETNCapSeats + BTechStudentDataELCapSeats + BTechStudentDataMECapSeats + BTechStudentDataITCapSeats + BTechStudentDataCSECapSeats,
        "BTechStudentDataTotalWhmtTrust": BTechStudentDataCVWhmtTrust + BTechStudentDataETNWhmtTrust + BTechStudentDataELWhmtTrust + BTechStudentDataMEWhmtTrust + BTechStudentDataITWhmtTrust + BTechStudentDataCSEWhmtTrust,
        "BTechStudentDataTotalDdTrust": BTechStudentDataCVDdTrust + BTechStudentDataETNDdTrust + BTechStudentDataELDdTrust + BTechStudentDataMEDdTrust + BTechStudentDataITDdTrust + BTechStudentDataCSEDdTrust,
        "BTechStudentDataTotalEws": BTechStudentDataCVEws + BTechStudentDataETNEws + BTechStudentDataELEws + BTechStudentDataMEEws + BTechStudentDataITEws + BTechStudentDataCSEEws,
        "BTechStudentDataTotalTfws": BTechStudentDataCVTfws + BTechStudentDataETNTfws + BTechStudentDataELTfws + BTechStudentDataMETfws + BTechStudentDataITTfws + BTechStudentDataCSETfws,
        "BTechStudentDataTotalJnK1": BTechStudentDataCVJnK1 + BTechStudentDataETNJnK1 + BTechStudentDataELJnK1 + BTechStudentDataMEJnK1 + BTechStudentDataITJnK1 + BTechStudentDataCSEJnK1,
        "BTechStudentDataTotalJnK2": BTechStudentDataCVJnK2 + BTechStudentDataETNJnK2 + BTechStudentDataELJnK2 + BTechStudentDataMEJnK2 + BTechStudentDataITJnK2 + BTechStudentDataCSEJnK2,
        "BTechStudentDataTotalNri": BTechStudentDataCVNri + BTechStudentDataETNNri + BTechStudentDataELNri + BTechStudentDataMENri + BTechStudentDataITNri + BTechStudentDataCSENri,
        "BTechStudentDataTotalPmsss": BTechStudentDataCVPmsss + BTechStudentDataETNPmsss + BTechStudentDataELPmsss + BTechStudentDataMEPmsss + BTechStudentDataITPmsss + BTechStudentDataCSEPmsss,
        "BTechStudentDataTotalNeut": BTechStudentDataCVNeut + BTechStudentDataETNNeut + BTechStudentDataELNeut + BTechStudentDataMENeut + BTechStudentDataITNeut + BTechStudentDataCSENeut,
        "BTechStudentDataTotalCatTotal": BTechStudentDataCVCatTotal + BTechStudentDataETNCatTotal + BTechStudentDataELCatTotal + BTechStudentDataMECatTotal + BTechStudentDataITCatTotal + BTechStudentDataCSECatTotal,

        "BTechStudentDataCSEOpenMale": BTechStudentDataCSEOpenMale,
        "BTechStudentDataCSEOpenFemale": BTechStudentDataCSEOpenFemale,
        "BTechStudentDataCSESCMale": BTechStudentDataCSESCMale,
        "BTechStudentDataCSESCFemale": BTechStudentDataCSESCFemale,
        "BTechStudentDataCSESTMale": BTechStudentDataCSESTMale,
        "BTechStudentDataCSESTFemale": BTechStudentDataCSESTFemale,
        "BTechStudentDataCSEVJNTMale": BTechStudentDataCSEVJNTMale,
        "BTechStudentDataCSEVJNTFemale": BTechStudentDataCSEVJNTFemale,
        "BTechStudentDataCSEOBCMale": BTechStudentDataCSEOBCMale,
        "BTechStudentDataCSEOBCFemale": BTechStudentDataCSEOBCFemale,
        "BTechStudentDataCSESBCMale": BTechStudentDataCSESBCMale,
        "BTechStudentDataCSESBCFemale": BTechStudentDataCSESBCFemale,
        "BTechStudentDataCSECatMFTotal": BTechStudentDataCSECatMFTotal,

        "BTechStudentDataITOpenMale": BTechStudentDataITOpenMale,
        "BTechStudentDataITOpenFemale": BTechStudentDataITOpenFemale,
        "BTechStudentDataITSCMale": BTechStudentDataITSCMale,
        "BTechStudentDataITSCFemale": BTechStudentDataITSCFemale,
        "BTechStudentDataITSTMale": BTechStudentDataITSTMale,
        "BTechStudentDataITSTFemale": BTechStudentDataITSTFemale,
        "BTechStudentDataITVJNTMale": BTechStudentDataITVJNTMale,
        "BTechStudentDataITVJNTFemale": BTechStudentDataITVJNTFemale,
        "BTechStudentDataITOBCMale": BTechStudentDataITOBCMale,
        "BTechStudentDataITOBCFemale": BTechStudentDataITOBCFemale,
        "BTechStudentDataITSBCMale": BTechStudentDataITSBCMale,
        "BTechStudentDataITSBCFemale": BTechStudentDataITSBCFemale,
        "BTechStudentDataITCatMFTotal": BTechStudentDataITCatMFTotal,

        "BTechStudentDataCVOpenMale": BTechStudentDataCVOpenMale,
        "BTechStudentDataCVOpenFemale": BTechStudentDataCVOpenFemale,
        "BTechStudentDataCVSCMale": BTechStudentDataCVSCMale,
        "BTechStudentDataCVSCFemale": BTechStudentDataCVSCFemale,
        "BTechStudentDataCVSTMale": BTechStudentDataCVSTMale,
        "BTechStudentDataCVSTFemale": BTechStudentDataCVSTFemale,
        "BTechStudentDataCVVJNTMale": BTechStudentDataCVVJNTMale,
        "BTechStudentDataCVVJNTFemale": BTechStudentDataCVVJNTFemale,
        "BTechStudentDataCVOBCMale": BTechStudentDataCVOBCMale,
        "BTechStudentDataCVOBCFemale": BTechStudentDataCVOBCFemale,
        "BTechStudentDataCVSBCMale": BTechStudentDataCVSBCMale,
        "BTechStudentDataCVSBCFemale": BTechStudentDataCVSBCFemale,
        "BTechStudentDataCVCatMFTotal": BTechStudentDataCVCatMFTotal,

        "BTechStudentDataMEOpenMale": BTechStudentDataMEOpenMale,
        "BTechStudentDataMEOpenFemale": BTechStudentDataMEOpenFemale,
        "BTechStudentDataMESCMale": BTechStudentDataMESCMale,
        "BTechStudentDataMESCFemale": BTechStudentDataMESCFemale,
        "BTechStudentDataMESTMale": BTechStudentDataMESTMale,
        "BTechStudentDataMESTFemale": BTechStudentDataMESTFemale,
        "BTechStudentDataMEVJNTMale": BTechStudentDataMEVJNTMale,
        "BTechStudentDataMEVJNTFemale": BTechStudentDataMEVJNTFemale,
        "BTechStudentDataMEOBCMale": BTechStudentDataMEOBCMale,
        "BTechStudentDataMEOBCFemale": BTechStudentDataMEOBCFemale,
        "BTechStudentDataMESBCMale": BTechStudentDataMESBCMale,
        "BTechStudentDataMESBCFemale": BTechStudentDataMESBCFemale,
        "BTechStudentDataMECatMFTotal": BTechStudentDataMECatMFTotal,

        "BTechStudentDataELOpenMale": BTechStudentDataELOpenMale,
        "BTechStudentDataELOpenFemale": BTechStudentDataELOpenFemale,
        "BTechStudentDataELSCMale": BTechStudentDataELSCMale,
        "BTechStudentDataELSCFemale": BTechStudentDataELSCFemale,
        "BTechStudentDataELSTMale": BTechStudentDataELSTMale,
        "BTechStudentDataELSTFemale": BTechStudentDataELSTFemale,
        "BTechStudentDataELVJNTMale": BTechStudentDataELVJNTMale,
        "BTechStudentDataELVJNTFemale": BTechStudentDataELVJNTFemale,
        "BTechStudentDataELOBCMale": BTechStudentDataELOBCMale,
        "BTechStudentDataELOBCFemale": BTechStudentDataELOBCFemale,
        "BTechStudentDataELSBCMale": BTechStudentDataELSBCMale,
        "BTechStudentDataELSBCFemale": BTechStudentDataELSBCFemale,
        "BTechStudentDataELCatMFTotal": BTechStudentDataELCatMFTotal,

        "BTechStudentDataETNOpenMale": BTechStudentDataETNOpenMale,
        "BTechStudentDataETNOpenFemale": BTechStudentDataETNOpenFemale,
        "BTechStudentDataETNSCMale": BTechStudentDataETNSCMale,
        "BTechStudentDataETNSCFemale": BTechStudentDataETNSCFemale,
        "BTechStudentDataETNSTMale": BTechStudentDataETNSTMale,
        "BTechStudentDataETNSTFemale": BTechStudentDataETNSTFemale,
        "BTechStudentDataETNVJNTMale": BTechStudentDataETNVJNTMale,
        "BTechStudentDataETNVJNTFemale": BTechStudentDataETNVJNTFemale,
        "BTechStudentDataETNOBCMale": BTechStudentDataETNOBCMale,
        "BTechStudentDataETNOBCFemale": BTechStudentDataETNOBCFemale,
        "BTechStudentDataETNSBCMale": BTechStudentDataETNSBCMale,
        "BTechStudentDataETNSBCFemale": BTechStudentDataETNSBCFemale,
        "BTechStudentDataETNCatMFTotal": BTechStudentDataETNCatMFTotal,

        "BTechStudentDataOpenMaleTotal": BTechStudentDataCSEOpenMale + BTechStudentDataMEOpenMale + BTechStudentDataCVOpenMale + BTechStudentDataITOpenMale + BTechStudentDataELOpenMale + BTechStudentDataETNOpenMale,
        "BTechStudentDataOpenFemaleTotal": BTechStudentDataCSEOpenFemale + BTechStudentDataMEOpenFemale + BTechStudentDataCVOpenFemale + BTechStudentDataITOpenFemale + BTechStudentDataELOpenFemale + BTechStudentDataETNOpenFemale,
        "BTechStudentDataSCMaleTotal": BTechStudentDataCSESCMale + BTechStudentDataMESCMale + BTechStudentDataCVSCMale + BTechStudentDataITSCMale + BTechStudentDataELSCMale + BTechStudentDataETNSCMale,
        "BTechStudentDataSCFemaleTotal": BTechStudentDataCSESCFemale + BTechStudentDataMESCFemale + BTechStudentDataCVSCFemale + BTechStudentDataITSCFemale + BTechStudentDataELSCFemale + BTechStudentDataETNSCFemale,
        "BTechStudentDataSTMaleTotal": BTechStudentDataCSESTMale + BTechStudentDataMESTMale + BTechStudentDataCVSTMale + BTechStudentDataITSTMale + BTechStudentDataELSTMale + BTechStudentDataETNSTMale,
        "BTechStudentDataSTFemaleTotal": BTechStudentDataCSESTFemale + BTechStudentDataMESTFemale + BTechStudentDataCVSTFemale + BTechStudentDataITSTFemale + BTechStudentDataELSTFemale + BTechStudentDataETNSTFemale,
        "BTechStudentDataVJNTMaleTotal": BTechStudentDataCSEVJNTMale + BTechStudentDataMEVJNTMale + BTechStudentDataCVVJNTMale + BTechStudentDataITVJNTMale + BTechStudentDataELVJNTMale + BTechStudentDataETNVJNTMale,
        "BTechStudentDataVJNTFemaleTotal": BTechStudentDataCSEVJNTFemale + BTechStudentDataMEVJNTFemale + BTechStudentDataCVVJNTFemale + BTechStudentDataITVJNTFemale + BTechStudentDataELVJNTFemale + BTechStudentDataETNVJNTFemale,
        "BTechStudentDataOBCMaleTotal": BTechStudentDataCSEOBCMale + BTechStudentDataMEOBCMale + BTechStudentDataCVOBCMale + BTechStudentDataITOBCMale + BTechStudentDataELOBCMale + BTechStudentDataETNOBCMale,
        "BTechStudentDataOBCFemaleTotal": BTechStudentDataCSEOBCFemale + BTechStudentDataMEOBCFemale + BTechStudentDataCVOBCFemale + BTechStudentDataITOBCFemale + BTechStudentDataELOBCFemale + BTechStudentDataETNOBCFemale,
        "BTechStudentDataSBCMaleTotal": BTechStudentDataCSESBCMale + BTechStudentDataMESBCMale + BTechStudentDataCVSBCMale + BTechStudentDataITSBCMale + BTechStudentDataELSBCMale + BTechStudentDataETNSBCMale,
        "BTechStudentDataSBCFemaleTotal": BTechStudentDataCSESBCFemale + BTechStudentDataMESBCFemale + BTechStudentDataCVSBCFemale + BTechStudentDataITSBCFemale + BTechStudentDataELSBCFemale + BTechStudentDataETNSBCFemale,
        "BTechStudentDataFinalCatMFTotal": BTechStudentDataETNCatMFTotal + BTechStudentDataELCatMFTotal + BTechStudentDataMECatMFTotal + BTechStudentDataITCatMFTotal + BTechStudentDataCVCatMFTotal + BTechStudentDataCSECatMFTotal,

        "BTechStudentDataCSEHighestPer": BTechStudentDataCSEHighestPer,
        "BTechStudentDataCVHighestPer": BTechStudentDataCVHighestPer,
        "BTechStudentDataMEHighestPer": BTechStudentDataMEHighestPer,
        "BTechStudentDataITHighestPer": BTechStudentDataITHighestPer,
        "BTechStudentDataELHighestPer": BTechStudentDataELHighestPer,
        "BTechStudentDataETNHighestPer": BTechStudentDataETNHighestPer,

        "BTechStudentDataCSELowestPer": BTechStudentDataCSELowestPer,
        "BTechStudentDataCVLowestPer": BTechStudentDataCVLowestPer,
        "BTechStudentDataITLowestPer": BTechStudentDataITLowestPer,
        "BTechStudentDataMELowestPer": BTechStudentDataMELowestPer,
        "BTechStudentDataELLowestPer": BTechStudentDataELLowestPer,
        "BTechStudentDataETNLowestPer": BTechStudentDataETNLowestPer,

        "BTechStudentDataCSEMale": BTechStudentDataCSEMale,
        "BTechStudentDataCSEFemale": BTechStudentDataCSEFemale,
        "BTechStudentDataCVMale": BTechStudentDataCVMale,
        "BTechStudentDataCVFemale": BTechStudentDataCVFemale,
        "BTechStudentDataITMale": BTechStudentDataITMale,
        "BTechStudentDataITFemale": BTechStudentDataITFemale,
        "BTechStudentDataMEMale": BTechStudentDataMEMale,
        "BTechStudentDataMEFemale": BTechStudentDataMEFemale,
        "BTechStudentDataELMale": BTechStudentDataELMale,
        "BTechStudentDataELFemale": BTechStudentDataELFemale,
        "BTechStudentDataETNMale": BTechStudentDataETNMale,
        "BTechStudentDataETNFemale": BTechStudentDataETNFemale,

        "CSETotalMF": CSETotalMF,
        "CVTotalMF": CVTotalMF,
        "METotalMF": METotalMF,
        "ITTotalMF": ITTotalMF,
        "ELTotalMF": ELTotalMF,
        "ETNTotalMF": ETNTotalMF,

        "TotalM": TotalM,
        "TotalF": TotalF,
        "TotalMF": TotalMF,

        "allResearchPapersCSE": allResearchPapersCSE,
        "countRPCSE": len(allResearchPapersCSE),
        "allResearchPapersCV": allResearchPapersCV,
        "countRPCV": len(allResearchPapersCV),
        "allResearchPapersME": allResearchPapersME,
        "countRPME": len(allResearchPapersME),
        "allResearchPapersIT": allResearchPapersIT,
        "countRPIT": len(allResearchPapersIT),
        "allResearchPapersEL": allResearchPapersEL,
        "countRPEL": len(allResearchPapersEL),
        "allResearchPapersETN": allResearchPapersETN,
        "countRPETN": len(allResearchPapersETN),
        "totalRP": len(allResearchPapersCSE) + len(allResearchPapersCV) + len(allResearchPapersME) + len(allResearchPapersIT) + len(allResearchPapersEL) + len(allResearchPapersETN),

        "allBookPublishedCSE": allBookPublishedCSE,
        "countBookPCSE": len(allBookPublishedCSE),
        "allBookPublishedCV": allBookPublishedCV,
        "countBookPCV": len(allBookPublishedCV),
        "allBookPublishedME": allBookPublishedME,
        "countBookPME": len(allBookPublishedME),
        "allBookPublishedIT": allBookPublishedIT,
        "countBookPIT": len(allBookPublishedIT),
        "allBookPublishedEL": allBookPublishedEL,
        "countBookPEL": len(allBookPublishedEL),
        "allBookPublishedETN": allBookPublishedETN,
        "countBookPETN": len(allBookPublishedETN),
        "totalBookP": len(allBookPublishedCSE) + len(allBookPublishedCV) + len(allBookPublishedME) + len(allBookPublishedIT) + len(allBookPublishedEL) + len(allBookPublishedETN),

        "allPatentsCSE": allPatentsCSE.filter(awarded=True),
        "countPatentsCSE": len(allPatentsCSE),
        "allPatentsCV": allPatentsCV.filter(awarded=True),
        "countPatentsCV": len(allPatentsCV),
        "allPatentsME": allPatentsME.filter(awarded=True),
        "countPatentsME": len(allPatentsME),
        "allPatentsIT": allPatentsIT.filter(awarded=True),
        "countPatentsIT": len(allPatentsIT),
        "allPatentsEL": allPatentsEL.filter(awarded=True),
        "countPatentsEL": len(allPatentsEL),
        "allPatentsETN": allPatentsETN.filter(awarded=True),
        "countPatentsETN": len(allPatentsETN),
        "totalPatents": len(allPatentsCSE) + len(allPatentsCV) + len(allPatentsME) + len(allPatentsIT) + len(allPatentsEL) + len(allPatentsETN),

        "allPatentsNACSE": allPatentsCSE.filter(awarded=False),
        "allPatentsNACV": allPatentsCV.filter(awarded=False),
        "allPatentsNAME": allPatentsME.filter(awarded=False),
        "allPatentsNAIT": allPatentsIT.filter(awarded=False),
        "allPatentsNAEL": allPatentsEL.filter(awarded=False),
        "allPatentsNAETN": allPatentsETN.filter(awarded=False),

        "allCompletedPHDCSE": allCompletedPHDCSE,
        "allCompletedPHDCV": allCompletedPHDCV,
        "allCompletedPHDIT": allCompletedPHDIT,
        "allCompletedPHDME": allCompletedPHDME,
        "allCompletedPHDEL": allCompletedPHDEL,
        "allCompletedPHDETN": allCompletedPHDETN,

        "allOngoingPHDCV": allOngoingPHDCV,
        "allOngoingPHDIT": allOngoingPHDIT,
        "allOngoingPHDCSE": allOngoingPHDCSE,
        "allOngoingPHDME": allOngoingPHDME,
        "allOngoingPHDEL": allOngoingPHDEL,
        "allOngoingPHDETN": allOngoingPHDETN,

        "allFacCompCourseCV": allFacCompCourseCV,
        "allFacCompCourseIT": allFacCompCourseIT,
        "allFacCompCourseCSE": allFacCompCourseCSE,
        "allFacCompCourseME": allFacCompCourseME,
        "allFacCompCourseEL": allFacCompCourseEL,
        "allFacCompCourseETN": allFacCompCourseETN,

        "allPhdStudentOtherCV": allPhdStudentOtherCV,
        "allPhdStudentOtherIT": allPhdStudentOtherIT,
        "allPhdStudentOtherCSE": allPhdStudentOtherCSE,
        "allPhdStudentOtherME": allPhdStudentOtherME,
        "allPhdStudentOtherEL": allPhdStudentOtherEL,
        "allPhdStudentOtherETN": allPhdStudentOtherETN,

        "allPhdStudentQIPCV": allPhdStudentQIPCV,
        "allPhdStudentQIPIT": allPhdStudentQIPIT,
        "allPhdStudentQIPCSE": allPhdStudentQIPCSE,
        "allPhdStudentQIPME": allPhdStudentQIPME,
        "allPhdStudentQIPEL": allPhdStudentQIPEL,
        "allPhdStudentQIPETN": allPhdStudentQIPETN,

        "allPhdStudentNDFCV": allPhdStudentNDFCV,
        "allPhdStudentNDFIT": allPhdStudentNDFIT,
        "allPhdStudentNDFCSE": allPhdStudentNDFCSE,
        "allPhdStudentNDFME": allPhdStudentNDFME,
        "allPhdStudentNDFEL": allPhdStudentNDFEL,
        "allPhdStudentNDFETN": allPhdStudentNDFETN,

        "allGoogleCitationCV": allGoogleCitationCV,
        "allGoogleCitationIT": allGoogleCitationIT,
        "allGoogleCitationCSE": allGoogleCitationCSE,
        "allGoogleCitationME": allGoogleCitationME,
        "allGoogleCitationEL": allGoogleCitationEL,
        "allGoogleCitationETN": allGoogleCitationETN,

        "allGuestLecOrganizedCV": allGuestLecOrganizedCV,
        "allGuestLecOrganizedIT": allGuestLecOrganizedIT,
        "allGuestLecOrganizedCSE": allGuestLecOrganizedCSE,
        "allGuestLecOrganizedME": allGuestLecOrganizedME,
        "allGuestLecOrganizedEL": allGuestLecOrganizedEL,
        "allGuestLecOrganizedETN": allGuestLecOrganizedETN,

        "allGuestLecDeliveredCV": allGuestLecDeliveredCV,
        "allGuestLecDeliveredIT": allGuestLecDeliveredIT,
        "allGuestLecDeliveredCSE": allGuestLecDeliveredCSE,
        "allGuestLecDeliveredME": allGuestLecDeliveredME,
        "allGuestLecDeliveredEL": allGuestLecDeliveredEL,
        "allGuestLecDeliveredETN": allGuestLecDeliveredETN,

        "allEventConductedCV": allEventConductedCV,
        "allEventConductedIT": allEventConductedIT,
        "allEventConductedCSE": allEventConductedCSE,
        "allEventConductedME": allEventConductedME,
        "allEventConductedEL": allEventConductedEL,
        "allEventConductedETN": allEventConductedETN,

        "allEventAttendedCV": allEventAttendedCV,
        "allEventAttendedIT": allEventAttendedIT,
        "allEventAttendedCSE": allEventAttendedCSE,
        "allEventAttendedME": allEventAttendedME,
        "allEventAttendedEL": allEventAttendedEL,
        "allEventAttendedETN": allEventAttendedETN,

        "SerialNoRSPCSE": SerialNoRSPCSE,
        "SerialNoRSPCV": SerialNoRSPCV,
        "SerialNoRSPIT": SerialNoRSPIT,
        "SerialNoRSPME": SerialNoRSPME,
        "SerialNoRSPEL": SerialNoRSPEL,
        "SerialNoRSPETN": SerialNoRSPCSE,

        "SerialNoPHDCSE": SerialNoPHDCSE,
        "SerialNoPHDCV": SerialNoPHDCV,
        "SerialNoPHDIT": SerialNoPHDIT,
        "SerialNoPHDME": SerialNoPHDME,
        "SerialNoPHDEL": SerialNoPHDEL,
        "SerialNoPHDETN": SerialNoPHDETN,

        "SerialNoOngoingPHDCSE": SerialNoOngoingPHDCSE,
        "SerialNoOngoingPHDCV": SerialNoOngoingPHDCV,
        "SerialNoOngoingPHDIT": SerialNoOngoingPHDIT,
        "SerialNoOngoingPHDME": SerialNoOngoingPHDME,
        "SerialNoOngoingPHDEL": SerialNoOngoingPHDEL,
        "SerialNoOngoingPHDETN": SerialNoOngoingPHDETN,

        "SerialNoBookPublishedCSE": SerialNoBookPublishedCSE,
        "SerialNoBookPublishedCV": SerialNoBookPublishedCV,
        "SerialNoBookPublishedIT": SerialNoBookPublishedIT,
        "SerialNoBookPublishedME": SerialNoBookPublishedME,
        "SerialNoBookPublishedEL": SerialNoBookPublishedEL,
        "SerialNoBookPublishedETN": SerialNoBookPublishedETN,

        "SerialNoFacCompCourseCSE": SerialNoFacCompCourseCSE,
        "SerialNoFacCompCourseCV": SerialNoFacCompCourseCV,
        "SerialNoFacCompCourseIT": SerialNoFacCompCourseIT,
        "SerialNoFacCompCourseME": SerialNoFacCompCourseME,
        "SerialNoFacCompCourseEL": SerialNoFacCompCourseEL,
        "SerialNoFacCompCourseETN": SerialNoFacCompCourseETN,

        "SerialNoPhdStudentOtherCSE": SerialNoPhdStudentOtherCSE,
        "SerialNoPhdStudentOtherCV": SerialNoPhdStudentOtherCV,
        "SerialNoPhdStudentOtherIT": SerialNoPhdStudentOtherIT,
        "SerialNoPhdStudentOtherME": SerialNoPhdStudentOtherME,
        "SerialNoPhdStudentOtherEL": SerialNoPhdStudentOtherEL,
        "SerialNoPhdStudentOtherETN": SerialNoPhdStudentOtherETN,

        "SerialNoPhdStudentQIPCSE": SerialNoPhdStudentQIPCSE,
        "SerialNoPhdStudentQIPCV": SerialNoPhdStudentQIPCV,
        "SerialNoPhdStudentQIPIT": SerialNoPhdStudentQIPIT,
        "SerialNoPhdStudentQIPME": SerialNoPhdStudentQIPME,
        "SerialNoPhdStudentQIPEL": SerialNoPhdStudentQIPEL,
        "SerialNoPhdStudentQIPETN": SerialNoPhdStudentQIPETN,

        "SerialNoPhdStudentNDFCSE": SerialNoPhdStudentNDFCSE,
        "SerialNoPhdStudentNDFCV": SerialNoPhdStudentNDFCV,
        "SerialNoPhdStudentNDFIT": SerialNoPhdStudentNDFIT,
        "SerialNoPhdStudentNDFME": SerialNoPhdStudentNDFME,
        "SerialNoPhdStudentNDFEL": SerialNoPhdStudentNDFEL,
        "SerialNoPhdStudentNDFETN": SerialNoPhdStudentNDFETN,

        "fromYear": fromYear,
        "toYear": int(toYear)+1,
    }
    pdf = render_to_pdf('pdfReportGenerate.html', args)
    # if pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     filename = 'Invoice1'
    #     content = "inline; filename='%s'" % (filename)
    #     download = request.GET.get("download")
    #     if download:
    #         content = "attachment; filename= %s" % (filename)
    #     response['Content-Disposition'] = content
    #     return response
    return HttpResponse(pdf, content_type='application/pdf')


@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a, b)
