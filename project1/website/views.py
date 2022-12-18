from django.http import HttpResponse
from django.shortcuts import render
from website import views
from website.models import enquiry_table
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return  render(request,'index.html')
    
def contactus(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        enquiry = enquiry_table(name=name, email=email, phone=phone, address=address)
        enquiry.save()
    return  render(request,'contactus.html')

def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'dashboard.html')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'In-correct username or password!')
            return render(request, 'registration/login.html')

    
    return  render(request,'login.html')

def dashboard(request):
    return  render(request,'dashboard.html')
    
