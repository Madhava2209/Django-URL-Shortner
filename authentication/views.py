from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def signup(request):
    if request.method=="POST":
        username =request.POST["user_name"]
        email =request.POST["email"]
        if User.objects.filter(username=username):
            return render(request,"signup.html",{"error":"Username not available"})
        if User.objects.filter(email=email):
            return render(request,"signup.html",{"email":"Email is already registered"})
        password =request.POST["password"]
        

        user=User.objects.create_user(username=username,email=email,password=password)

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
            return render(request,'login.html',{"error":"Provide valid credentials"})
    return render(request,"login.html")

def signout(request):
    logout(request)
    return redirect("/login/")


