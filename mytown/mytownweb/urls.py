from django.urls import path
from .views import contactus , thankyou

urlpatterns=[
    path('contactus/', contactus , name='contactus'),
    path('thankyou/' , thankyou , name='thankyou'),
]