from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

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