from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password == conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching...')

        return redirect('register')

    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if request.user.groups.filter(name="Admin").exists():
                return redirect('adminApp:adminHome')
            elif request.user.groups.filter(name="CSE").exists():
                return redirect('CSE:teacherHome')
            elif request.user.groups.filter(name="IT").exists():
                return redirect('IT:teacherHome')
            elif request.user.groups.filter(name="Civil").exists():
                return redirect('Civil:teacherHome')
            elif request.user.groups.filter(name="ME").exists():
                return redirect('ME:teacherHome')
            elif request.user.groups.filter(name="Electrical").exists():
                return redirect('Electrical:teacherHome')
            elif request.user.groups.filter(name="Electronics").exists():
                return redirect('Electronics:teacherHome')
            else:
                auth.logout(request)
                messages.info(request, 'You are not assign any Department, Please contact Admin.')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Invalid Credential')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


