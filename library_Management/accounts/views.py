from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as ulogout
from .form_vailadition import check_mobile,check_name,check_email
from django.contrib import messages
from .models import User
# Create your views here.
def user_Signup(request):
    """This function is resposible to Signup for student not admin"""
    if not request.user.is_authenticated:
        if request.method == "POST":
            sname = request.POST.get("sname")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if sname and email and mobile and password1 and password2:
                if password1 == password2:
                    if check_mobile(mobile):
                        if check_email(email):
                            if check_name(sname):
                                check_usnique_mail = User.objects.filter(email=email)
                                if not check_usnique_mail:
                                    User.objects.create_user(email, password1, sname, mobile)
                                    messages.error(request, "Accounts has been created!")
                                else:
                                    messages.error(request, "Ragister with another email id!")

                            else:
                                messages.error(request, "name should be alphabatical form!")
                        else:
                            messages.error(request, "enter a vailed Email Id!")
                    else:
                        messages.error(request, "Mobile number should be 10 digit and digit form!")
                else:
                    messages.error(request, "password does not matched!")
            else:
                messages.error(request, "fill required field!")
        return render(request, 'signup.html')
    else:
        return redirect("/library")

def login(request):
    """This function is resposible to login for student not admin"""
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            if email and password:
                if check_email(email):
                    authenticated_user = authenticate(username=email, password=password)
                    if authenticated_user:
                        ulogin(request, authenticated_user)
                        return redirect("/library")
                    else:
                        messages.error(request, 'invailed creadientials!')
                else:
                    messages.error(request, "enter a valiled email!")
            else:
                messages.error(request, "fill required all fields!")

        return render(request, "login.html")
    else:
        return redirect("/library")


def logout(request):
    """this functions is resposible to lgout from student side """
    if request.user.is_authenticated:
        ulogout(request)
        return redirect("/login")
    else:
        redirect("/library")
