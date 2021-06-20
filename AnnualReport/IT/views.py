import csv
from django.contrib import messages
from io import TextIOWrapper

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from IT.models import PHD, BTechStudentData, ResearchPaperMain, ResearchPaperUser, Teacher, BookPublished, Patents, \
    FacultyCompletedCourse, GuideforPHD, GoogleScholarCitationDetails, GuestLecOrganizedOrDelivered, EventConductedOrAttended


def isAuthenticatedDepartment(request):
    if request.user.groups.filter(name="IT").exists():
        return True
    else:
        return False


def teacherHome(request):
    if isAuthenticatedDepartment(request):
        return render(request, "teacherHome.html", {'depart': "IT"})
    return HttpResponse("<h1>Page Not Found</h1>")


def teacherProfile(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        teacherData = Teacher.objects.filter(user=user)
        if teacherData.exists():
            teacherData = Teacher.objects.get(user=user)
        return render(request, "teacherProfile.html", {'teacherData': teacherData})
    return HttpResponse("<h1>Page Not Found</h1>")


def editTeacherProfile(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            age = request.POST['age']
            address1_permanent = request.POST['permanent_address']
            address2_optional = request.POST['correspondence_address']
            college_post = request.POST['college_post']
            teaching_type = request.POST['teaching_type']
            regular_contractual = request.POST['regular_contractual']
            department = request.POST['department']
            higher_education = request.POST['higher_education']
            gate_score = request.POST['gate_score']
            cat_score = request.POST['cat_score']
            gre_score = request.POST['gre_score']

            name = first_name + " " + last_name
            if age == '':
                age = 0
            if gate_score == '':
                gate_score = 0
            if cat_score == '':
                cat_score = 0
            if gre_score == '':
                gre_score = 0

            if Teacher.objects.filter(user=request.user).exists():
                user = request.user
                teacher = Teacher.objects.get(user=user)

                user.first_name = first_name
                user.last_name = last_name
                teacher.name = name
                teacher.age = age
                teacher.address1_permanent = address1_permanent
                teacher.address2_optional = address2_optional
                teacher.college_post = college_post
                teacher.teaching_type = teaching_type
                if regular_contractual == "Regular":
                    teacher.regular_contractual = True
                else:
                    teacher.regular_contractual = False
                teacher.department = department
                teacher.higher_education = higher_education
                teacher.gate_score = gate_score
                teacher.cat_score = cat_score
                teacher.gre_score = gre_score

                user.save()
                teacher.save()
            else:
                if regular_contractual == "Regular":
                    teacherData = Teacher(user=request.user, name=name, age=age, address1_permanent=address1_permanent,
                                          address2_optional=address2_optional, college_post=college_post,
                                          teaching_type=teaching_type, regular_contractual=True, department=department,
                                          higher_education=higher_education, gate_score=gate_score, cat_score=cat_score,
                                          gre_score=gre_score)
                    teacherData.save()
                else:
                    teacherData = Teacher(user=request.user, name=name, age=age, address1_permanent=address1_permanent,
                                          address2_optional=address2_optional, college_post=college_post,
                                          teaching_type=teaching_type, regular_contractual=False, department=department,
                                          higher_education=higher_education, gate_score=gate_score, cat_score=cat_score,
                                          gre_score=gre_score)
                    teacherData.save()

            return redirect("IT:teacherProfile")

        user = request.user
        teacherData = Teacher.objects.filter(user=user)
        if teacherData.exists():
            teacherData = Teacher.objects.get(user=user)

        return render(request, "editTeacherProfile.html", {'teacherData': teacherData})
    return HttpResponse("<h1>Page Not Found</h1>")


def changePassword(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            currentPassword = request.POST['currentPassword']
            newPassword = request.POST['newPassword']
            confirmPassword = request.POST['confirmPassword']

            try:
                matchcheck = check_password(currentPassword, request.user.password)
                if matchcheck is False:
                    err = {}
                    err["error_message"] = "Entered Current Password is Incorrect. Please Retry."
                    return render(request, "changePassword.html", err)
                if newPassword != confirmPassword:
                    err = {}
                    err["error_message"] = "Entered New Passwords do not Match. Please Retry."
                    return render(request, "changePassword.html", err)
            except:
                err = {}
                err["error_message"] = "Refresh the Page to change the Password Again."
                return render(request, "changePassword.html", err)

            user = request.user
            user.set_password(newPassword)
            user.save()
            update_session_auth_hash(request, user)
            messages.info(request, 'Password changed successfully.')
            return redirect("IT:teacherHome")

        return render(request, "changePassword.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def researchPapers(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        allResearchDOI = ResearchPaperUser.objects.filter(user=user)

        allResearchPaper = []

        for i in allResearchDOI:
            temp = ResearchPaperMain.objects.filter(doi=i.doi)
            allResearchPaper.append(temp)

        # print(allResearchPaper[1][0].author_name)

        args = {}
        args["allResearchPaper"] = allResearchPaper
        args["len"] = len(allResearchPaper)

        return render(request, "researchPapers.html", args)
    return HttpResponse("<h1>Page Not Found</h1>")


def addResearchPapers(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            doi = request.POST['doi']
            type_of_publication = request.POST['type_of_publication']
            details_of_paper = request.POST['details_of_paper']
            author_name = request.POST['author_name']
            publication_date = request.POST['publication_date']
            department = request.POST['department']
            area_of_research = request.POST['area_of_research']
            publication_details = request.POST['publication_details']
            noOfAuthor = request.POST['noOfAuthor']
            user2 = request.POST['user2']
            user3 = request.POST['user3']
            academic_year = request.POST['academic_year']
            toYear = request.POST['toYear']

            if academic_year >= toYear:
                return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")

            if ResearchPaperMain.objects.filter(doi=doi).exists():
                messages.info(request, "Record Already Exist!")
                return redirect("IT:addResearchPapers")

            researchPaperData = ResearchPaperMain(doi=doi, type_of_publication=type_of_publication, details_of_paper=details_of_paper,
                                                  author_name=author_name, publication_date=publication_date, department=department,
                                                  area_of_research=area_of_research, publication_details=publication_details, academic_year=academic_year)
            researchPaperData.save()

            ResearchPaperUser(doi=doi, user=request.user).save()
            if noOfAuthor == "2":
                ResearchPaperUser(doi=doi, user=user2).save()
            if noOfAuthor == "3":
                ResearchPaperUser(doi=doi, user=user2).save()
                ResearchPaperUser(doi=doi, user=user3).save()

            return redirect("IT:researchPapers")

        return render(request, "addResearchPapers.html")
    return HttpResponse('<h1>Page Not Found</h1>')


def researchPaperDelete(request, doi):
    if isAuthenticatedDepartment(request):
        researchPaper = ResearchPaperMain.objects.get(doi=doi)
        researchPaper.delete()
        researchPaperUsers = ResearchPaperUser.objects.filter(doi=doi)
        researchPaperUsers.delete()

        return redirect("IT:researchPapers")
    return HttpResponse("<h1>Page Not Found</h1>")


def phdDetails(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        allPhd = PHD.objects.filter(user=user)
        args = {}
        args["allPhd"] = allPhd
        return render(request, "phdDetails.html", args)
    return HttpResponse("<h1>Page Not Found</h1>")


def addPHD(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            guide_name = request.POST['guide_name']
            registration_date = request.POST['registration_date']
            title = request.POST['title']
            status = request.POST['status']
            completion_date = request.POST['completion_date']

            name = request.user.first_name + " " + request.user.last_name

            if status == "Completed":
                phdData = PHD(user=request.user, department='Information Technology', guide_name=guide_name, faculty_name=name,
                              registration_date=registration_date, title=title, status=True,
                              completion_date=completion_date)
            else:
                phdData = PHD(user=request.user, department='Information Technology', guide_name=guide_name, faculty_name=name,
                              registration_date=registration_date, title=title, status=False)

            phdData.save()

            return redirect("IT:phdDetails")

        return render(request, "addPHD.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def phdDetailsDelete(request, id):
    if isAuthenticatedDepartment(request):
        phdData = PHD.objects.get(id=id)
        phdData.delete()
        return redirect("IT:phdDetails")
    return HttpResponse("<h1>Page Not Found</h1>")


def studentData(request):
    if isAuthenticatedDepartment(request):
        academic_year = request.POST['academic_year']
        toYear = request.POST['toYear']

        if academic_year >= toYear:
            return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")

        allStudent = BTechStudentData.objects.filter(academic_year=academic_year)
        # allStudent = BTechStudentData.objects.all()
        args = {}
        args["allStudent"] = allStudent
        return render(request, "studentData.html", args)
    return HttpResponse("<h1>Page Not Found</h1>")


def addStudentData(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            name = request.POST['name']
            PRN = request.POST['PRN']
            gender = request.POST['gender']
            address = request.POST['address']
            category = request.POST['category']
            fees_paid = request.POST['fees_paid']
            branch = request.POST['branch']
            clg_shift = request.POST['clg_shift']
            cet_Score = request.POST['cetScore']
            admission_type = request.POST['admission_type']
            academic_year = request.POST['academic_year']
            toYear = request.POST['toYear']

            if academic_year >= toYear:
                return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")
            student_data = BTechStudentData(name=name, PRN=PRN, gender=gender, address=address,
                                            category=category, fees_paid=fees_paid, branch=branch, clg_shift=clg_shift,
                                            CET_Score=cet_Score, admission_type=admission_type,
                                            academic_year=academic_year)
            student_data.save()

            return redirect("IT:teacherHome")

        return render(request, "addStudentData.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def importStudentData(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            upload_csv = request.FILES['upload_csv']
            upload_csv = TextIOWrapper(upload_csv.file, encoding=request.encoding)
            file_reader = csv.reader(upload_csv, delimiter=',')
            counter = 0

            for row in file_reader:
                # do something with row data.
                if counter == 0:
                    counter += 1
                    continue
                name = row[0]
                PRN = row[1]
                gender = row[2]
                address = row[3]
                category = row[4]
                fees_paid = row[5]
                branch = row[6]
                clg_shift = row[7]
                cet_Score = row[8]
                admission_type = row[9]
                academic_year = row[10]

                student_data = BTechStudentData(name=name, PRN=PRN, gender=gender, address=address,
                                                category=category, fees_paid=fees_paid, branch=branch,
                                                clg_shift=clg_shift,
                                                CET_Score=cet_Score, admission_type=admission_type,
                                                academic_year=academic_year)
                student_data.save()

            return redirect("IT:teacherHome")

        return render(request, "importStudentData.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def studentDataDelete(request, PRN):
    if isAuthenticatedDepartment(request):
        student_data = BTechStudentData.objects.get(PRN=PRN)
        student_data.delete()
        return redirect("IT:studentData")
    return HttpResponse("<h1>Page Not Found</h1>")


def bookPublished(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        allPublishedBooks = BookPublished.objects.filter(user=user)
        args = {}
        args["allPublishedBooks"] = allPublishedBooks
        return render(request, "bookPublished.html", args)
    return HttpResponse("<h1>Page Not Found</h1>")


def addBookPublished(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            name_faculty = request.POST['name_faculty']
            title_of_book = request.POST['title_of_book']
            name_of_publisher = request.POST['name_of_publisher']
            date_publication = request.POST['date_publication']
            academic_year = request.POST['academic_year']
            toYear = request.POST['toYear']

            if academic_year >= toYear:
                return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")
            bookPublish = BookPublished(user=request.user, name_faculty=name_faculty, title_of_book=title_of_book,
                                        name_of_publisher=name_of_publisher, date_publication=date_publication, academic_year=academic_year)
            bookPublish.save()
            return redirect("IT:bookPublished")

        return render(request, "addBookPublished.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def bookPublishedDelete(request, id):
    if isAuthenticatedDepartment(request):
        bookData = BookPublished.objects.get(id=id)
        bookData.delete()
        return redirect("IT:bookPublished")
    return HttpResponse("<h1>Page Not Found</h1>")


def patents(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        allPatents = Patents.objects.filter(user=user)
        args = {}
        args["allPatents"] = allPatents
        return render(request, "patents.html", args)
    return HttpResponse("<h1>Page Not Found</h1>")


def addPatents(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            name_faculty = request.POST['name_faculty']
            title = request.POST['title']
            patent_no = request.POST['patent_no']
            date_of_file = request.POST['date_of_file']
            awarded = request.POST['awarded']
            academic_year = request.POST['academic_year']
            toYear = request.POST['toYear']

            if academic_year >= toYear:
                return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")
            if Patents.objects.filter(patent_no=patent_no).exists():
                messages.info(request, "Record Already Exist!")
                return redirect("IT:addPatents")

            if awarded == "Yes":
                patent = Patents(user=request.user, name_faculty=name_faculty, title=title,
                                 patent_no=patent_no, date_of_file=date_of_file, awarded=True, academic_year=academic_year)
            else:
                patent = Patents(user=request.user, name_faculty=name_faculty, title=title,
                                 patent_no=patent_no, date_of_file=date_of_file, awarded=False, academic_year=academic_year)
            patent.save()
            return redirect("IT:patents")

        return render(request, "addPatents.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def patentsDelete(request, id):
    if isAuthenticatedDepartment(request):
        patentData = Patents.objects.get(id=id)
        patentData.delete()
        return redirect("IT:patents")
    return HttpResponse("<h1>Page Not Found</h1>")


def facultyCompletedCourse(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        allCourses = FacultyCompletedCourse.objects.filter(user=user)
        args = {}
        args["allCourses"] = allCourses
        return render(request, "facultyCompletedCourse.html", args)
    return HttpResponse("<h1>Page Not Found</h1>")


def addFacultyCompletedCourse(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            faculty_name = request.POST['faculty_name']
            title_course = request.POST['title_course']
            starting_date = request.POST['starting_date']
            completion_date = request.POST['completion_date']
            mode = request.POST['mode']
            academic_year = request.POST['academic_year']
            toYear = request.POST['toYear']

            if academic_year >= toYear:
                return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")
            completedCourse = FacultyCompletedCourse(user=request.user, faculty_name=faculty_name, title_course=title_course,
                                                     starting_date=starting_date, completion_date=completion_date, mode=mode, academic_year=academic_year)
            completedCourse.save()
            return redirect("IT:facultyCompletedCourse")

        return render(request, "addFacultyCompletedCourse.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def facultyCompletedCourseDelete(request, id):
    if isAuthenticatedDepartment(request):
        courseData = FacultyCompletedCourse.objects.get(id=id)
        courseData.delete()
        return redirect("IT:facultyCompletedCourse")
    return HttpResponse("<h1>Page Not Found</h1>")


def guidePhdDetails(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        guideAllPhd = GuideforPHD.objects.filter(user=user)
        args = {}
        args["guideAllPhd"] = guideAllPhd
        return render(request, "guidePhdDetails.html", args)
    return HttpResponse("<h1>Page Not Found</h1>")


def guideAddPHD(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            student_name = request.POST['student_name']
            registration_date = request.POST['registration_date']
            title_thesis = request.POST['title_thesis']
            guide_name = request.POST['guide_name']
            comment_on_thesis = request.POST['comment_on_thesis']
            type_of_phd = request.POST['type_of_phd']
            status = request.POST['status']
            completion_date = request.POST['completion_date']

            if status == "Completed":
                guidePhdData = GuideforPHD(user=request.user, student_name=student_name,
                                           registration_date=registration_date, title_thesis=title_thesis,
                                           guide_name=guide_name, comment_on_thesis=comment_on_thesis, type_of_phd=type_of_phd,
                                           status=True, completion_date=completion_date)

            else:
                guidePhdData = GuideforPHD(user=request.user, student_name=student_name,
                                           registration_date=registration_date, title_thesis=title_thesis,
                                           guide_name=guide_name, comment_on_thesis=comment_on_thesis, type_of_phd=type_of_phd,
                                           status=False)



            guidePhdData.save()
            return redirect("IT:guidePhdDetails")

        return render(request, "addGuidePHD.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def guidePhdDetailsDelete(request, id):
    if isAuthenticatedDepartment(request):
        guidePhdData = GuideforPHD.objects.get(id=id)
        guidePhdData.delete()
        return redirect("IT:guidePhdDetails")
    return HttpResponse("<h1>Page Not Found</h1>")



def googleScholarCitationDetails(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        googleAllCitationDetails = GoogleScholarCitationDetails.objects.filter(user=user)
        args = {}
        args["googleAllCitationDetails"] = googleAllCitationDetails
        return render(request, "googleScholarCitationDetails.html", args)
    return HttpResponse("<h1>Page Not Found</h1>")


def addGoogleScholarCitationDetails(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
            teacher_name = request.POST['teacher_name']
            designation = request.POST['designation']
            citations_2015 = request.POST['citations_2015']
            h_index_2015 = request.POST['h_index_2015']
            i_10_2015 = request.POST['i_10_2015']
            citations_all = request.POST['citations_all']
            h_index_all = request.POST['h_index_all']
            i_10_all = request.POST['i_10_all']
            cited_publication = request.POST['cited_publication']
            reported_publication = request.POST['reported_publication']
            academic_year = request.POST['academic_year']
            toYear = request.POST['toYear']

            if academic_year >= toYear:
                return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")

            if GoogleScholarCitationDetails.objects.filter(user=request.user).filter(academic_year=academic_year).exists():
                messages.info(request, "Record Already ! You can Add this Record only once in same acedmic year. If you want to update this record first delete previous Record and add new one!")
                return redirect("IT:addGoogleScholarCitationDetails")

            citationDetails = GoogleScholarCitationDetails(user=request.user, teacher_name=teacher_name, designation=designation, citations_2015=citations_2015,
                                                           h_index_2015=h_index_2015, i_10_2015=i_10_2015, citations_all=citations_all, h_index_all=h_index_all,
                                                           i_10_all=i_10_all, cited_publication=cited_publication, reported_publication=reported_publication, academic_year=academic_year)


            citationDetails.save()
            return redirect("IT:googleScholarCitationDetails")

        return render(request, "addGoogleScholarCitationDetails.html")
    return HttpResponse("<h1>Page Not Found</h1>")


def googleScholarCitationDetailsDelete(request, id):
    if isAuthenticatedDepartment(request):
        citationDetails = GoogleScholarCitationDetails.objects.get(id=id)
        citationDetails.delete()
        return redirect("IT:googleScholarCitationDetails")
    return HttpResponse("<h1>Page Not Found</h1>")


def guestLecOrganizedOrDelivered(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        allguestLecDetails = GuestLecOrganizedOrDelivered.objects.filter(user=user)
        args = {}
        args['allguestLecDetails'] = allguestLecDetails
        return render(request, 'guestLecOrganizedOrDelivered.html', args)
    return HttpResponse("<h1>Page Not Found</h1>")    


def addguestLecOrganizedOrDelivered(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
           teacher_name = request.POST['teacher_name'] 
           place = request.POST['place']
           subject = request.POST['subject']
           starting_date = request.POST['starting_date']
           ending_date = request.POST['ending_date']
           type = request.POST['type']
           academic_year = request.POST['academic_year']
           toYear = request.POST['toYear']

           if academic_year >= toYear:
               return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")
           guestLecDetails = GuestLecOrganizedOrDelivered(user=request.user, teacher_name=teacher_name, place=place, subject=subject, 
                                                            starting_date=starting_date, ending_date=ending_date, type=type, academic_year=academic_year)
                                                
           guestLecDetails.save()
           return redirect("IT:guestLecOrganizedOrDelivered")
        return render(request, "addguestLecOrganizedOrDelivered.html")
    return HttpResponse("<h1>Page Not Found</h1>")

def guestLecOrganizedOrDeliveredDelete(request, id):
    if isAuthenticatedDepartment(request):
        lectureDetails = GuestLecOrganizedOrDelivered.objects.get(id=id)
        lectureDetails.delete()
        return redirect("IT:guestLecOrganizedOrDelivered")
    return HttpResponse("<h1>Page Not Found</h1>")



def eventConductedOrAttended(request):
    if isAuthenticatedDepartment(request):
        user = request.user
        allEventDetails = EventConductedOrAttended.objects.filter(user=user)
        args = {}
        args['allEventDetails'] = allEventDetails
        return render(request, 'eventConductedOrAttended.html', args)
    return HttpResponse("<h1>Page Not Found</h1>")    


def addeventConductedOrAttended(request):
    if isAuthenticatedDepartment(request):
        if request.method == 'POST':
           teacher_name = request.POST['teacher_name'] 
           nameof_event = request.POST['nameof_event']
           event_details = request.POST['event_details']
           starting_date = request.POST['starting_date']
           ending_date = request.POST['ending_date']
           type_of_event = request.POST['type_of_event']
           academic_year = request.POST['academic_year']
           toYear = request.POST['toYear']


           if academic_year >= toYear:
               return HttpResponse("<h1>You have selected wrong Academic Year!</h1>")
           eventDetails = EventConductedOrAttended(user=request.user, teacher_name=teacher_name, nameof_event=nameof_event, event_details=event_details, 
                                                            starting_date=starting_date, ending_date=ending_date, type_of_event=type_of_event, academic_year=academic_year)
                                                
           eventDetails.save()
           return redirect("IT:eventConductedOrAttended")
        return render(request, "addeventConductedOrAttended.html")
    return HttpResponse("<h1>Page Not Found</h1>")

def eventConductedOrAttendedDelete(request, id):
    if isAuthenticatedDepartment(request):
        eventDetails = EventConductedOrAttended.objects.get(id=id)
        eventDetails.delete()
        return redirect("IT:guestLecOrganizedOrDelivered")
    return HttpResponse("<h1>Page Not Found</h1>")