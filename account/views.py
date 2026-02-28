from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import random
import string
from django.core.mail import EmailMessage

from django.conf import settings
# Create your views here.
def send_otp_to_mail(request,u_id):

    user = User.objects.filter(id = u_id).first()

    letter = string.digits
    otp =''.join(random.choices(letter, k=3))
    otp = int(otp)

    request.session['otp'] = otp
    request.session.set_expiry(300)


    email = EmailMessage(
    subject="Your OTP for Sing In",
    body=f"""
    Hello {user.username},

    Your One-Time Password (OTP) is: {otp}

    This OTP is valid for 5 minutes.
    Please do not share this OTP with anyone.

    If you did not request this, please ignore this email.

    Regards,
    Fruitables
    """,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )

    email.send()

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        otp = int(otp)
        session_otp = request.session.get('otp')

        if otp == session_otp:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request, "OTP is worng")
            return redirect("/account/sign_in/?otp=worng_otp")

def sign_in(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        global user 

        user = authenticate(request, username=username, password=password)

        if user:
            send_otp_to_mail(request,user.id)
            return render(request,"account/sign_in.html",{"username":username,"password":password,"enter_otp":True})

        if user is None:
            messages.info(request, "username or password is worng")
            return redirect("/account/sign_in/")
        else:
            login(request, user)
            return redirect("/")

    return render(request,"account/sign_in.html")

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        users = User.objects.all()

        for user in users:
            if username == user.username:
                messages.info(request, " username is already exit")
                return redirect("/account/sign_up/")
            
            elif email == user.email:
                messages.info(request, " email is already exit")
                return redirect("/account/sign_up/")
            
            elif password1 != password2:
                messages.info(request, "password do not match")
                return redirect("/account/sign_up/")
         
        
        new_users = User(username = username, email = email)
        new_users.set_password(password1)
        new_users.save()
        messages.info(request, "account create succesfully")
        return redirect("/account/sign_in/")

       
    return render(request, "account/sign_up.html")

def log_out(request):
    logout(request)
    return redirect("/account/sign_in/")