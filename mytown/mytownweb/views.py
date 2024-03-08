from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , redirect
from django.contrib import messages
from django.urls import reverse

from django.contrib.auth.models import User


def contactus(request):
    return render (request , 'contactus.html')

def thankyou (request):
    return HttpResponseRedirect(reverse('contactus'))



