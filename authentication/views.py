from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def signup(request):
    if request.method=="POST":
        username =request.POST["user_name"]
        email =request.POST["email"]
        password =request.POST["password"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]

        user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)

        login(request,user)

        return redirect("/dashboard/")
    return render(request,"signup.html")

def signin(request):
    if request.method=="POST":
        username=request.POST["user_name"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect("/dashboard/")
        else:
            return redirect('/login/')
    return render(request,"login.html")

def signout(request):
    logout(request)
    return redirect("/login/")


