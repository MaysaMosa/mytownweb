from django.urls  import path
# from .views import addreport
from . import views


urlpatterns = [
    path('workerlogin/', views.workerlogin,name="workerlogin"),
     path('addreports/', views.addreports,name="addreports"),


]
