from django.shortcuts import render
from .forms import Loginform
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
# Create your views here.

def login_user(request):
    if request.method == "POST":
        form=Loginform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd["username"],
                                password = cd["password"])
            if user is not None:
                login(request,user)
                return HttpResponse("Authentication succesfull")
            else:
                return HttpResponse("Authentication is not succesfull Please try again")
    else:
            form = Loginform()
    return render(request,"Loginuser.html",{"form":form})

