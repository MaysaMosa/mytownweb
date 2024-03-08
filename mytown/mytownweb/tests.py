# from django.forms import ValidationError
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.core.validators import EmailValidator
# from . import views 


# def signup(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         # Username validation (not empty)
#         if not username:
#             messages.error(request, "Username cannot be empty.")
#             return render(request, "mytown/signup.html")

#         # Email validation (@ symbol)
#         try:
#             validate_email = EmailValidator()
#             validate_email(email)
#         except ValidationError:
#             messages.error(request, "Please enter a valid email address.")
#             return render(request, "mytown/signup.html")

#         # Password validation (match)
#         if pass1 != pass2:
#             messages.error(request, "Passwords do not match.")
#             return render(request, "mytown/signup.html")

#         # Rest of your signup logic (creating user, etc.)

#         # Successful signup logic here (redirect, messages, etc.)

#     return render(request, "mytown/signup.html")
