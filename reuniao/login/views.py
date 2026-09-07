from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def login_view(request):
    return render(request,"login/login.html")