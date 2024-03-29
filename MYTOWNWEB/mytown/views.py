from django.shortcuts import redirect, render
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import admin
from .models import AddReport



def workerlogin(request):
       if request.method == "POST":
        username = request.POST.get('username', '')
        password= request.POST.get('password', '')
        myuser = User.objects.create(
            username=username,
            password=password,
         )
        messages.success(request, "user added successfully!")
        return redirect('workerlogin')
       
       return render(request, "acconut/workerlogin.html" )

def addreports(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        city = request.POST.get('city', '')
        description = request.POST.get('description', '')
        location = request.POST.get('location', '')
        picture = request.FILES.get('picture', None)

        # The error is likely here, where 'AddReport' is not assigned a value
        report = AddReport.objects.create(
            title=title,
            city=city,
            description=description,
            location=location,
            picture=picture
        )

        messages.success(request, "Report added successfully!")
        return redirect('addreports')

    return render(request, "account/addreports.html")
