from django.shortcuts import render,redirect
from django.contrib.auth import *
from shortner.models import *
import hashlib
from hashlib import blake2b
 
# Create your views here.
def home(request):
    return render(request,"home.html")


def dashboard(request):
    user=request.user
    url_instance=url.objects.filter(user=user)
    return render(request,'dashboard.html',{"link":url_instance})


def create_short_url(request):
    if request.method=="POST":
        user=request.user
        url_instance=url.objects.filter(user=user)
        title=request.POST["title"]
        long_url=request.POST["long_url"]
        #m = hashlib.sha256(str(long_url).encode('utf-8'))
        #m.digest()
        url_name=url.objects.filter(title=title)
        if url_name:
            return render(request,'dashboard.html',{"link":url_instance,"error":"not available"})
        m="my-url.herokuapp.com/" + title
        print(m)
        log=url.objects.create(
            title=title,
            long_url=long_url,
            short_hash=m,
            user=request.user,
            no_clicks=0,

        )
        return redirect('/dashboard/')


def redirect_to_long_url(request,hashcode):
    url_instance=url.objects.get(short_hash=hashcode)
    url_instance.no_clicks +=1  
    url_instance.save()
    long_url=url_instance.long_url
    return redirect(f"{long_url}/")







