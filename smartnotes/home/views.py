from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required 

#for class based view
from django.views.generic import TemplateView
# to create sigup page --> creating view
from django.views.generic import  CreateView
#to handle authentcation we import mixns class
from django.contrib.auth.mixins import LoginRequiredMixin
# to create login logout view
from django.contrib.auth.views import LoginView, LogoutView
# importing user creation class
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/login' #replace /smart/notes with /login

    def get (self,request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)



class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class HomeView (TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}

class AuthorisedView (LoginRequiredMixin,TemplateView):
    template_name = 'home/authorised.html'
    login_url = '/admin'







''''
def home (request):
    return render (request, 'home/welcome.html', {'today':datetime.today()})


@login_required(login_url='/admin')
def authorised (request):
    return render (request, 'home/authorised.html', {})
'''


# Create your views here.

