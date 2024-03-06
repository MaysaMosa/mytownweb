from django.shortcuts import render
from django.http import HttpResponse


def workerlogin(request):
      return render(request, 'workerlogin.html')
def addreports(request):
    return render(request, 'addreports.html')
