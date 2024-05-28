from django.shortcuts import render
from .models import News
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.exceptions import ValidationError
from main.forms import LoginUserForm,User,UserCreationForm,AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import RegisterUserForm
from .models import Menu

# Create your views here.
def index(request):
    results = News.objects.all()
    try:
        data = {
            "news": results
        }
        return render(request, "base.html", context=data)
    except:
        return HttpResponseNotFound(request, "pageNotFound404.html", status=404)


class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = '../templates/login.html'
    extra_context = {"title":'Авторизация','form':form_class}

    def get_success_url(self):
        return reverse_lazy('main_url') #Settings py
# Create your views here.

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('login')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('main_url')

def menu(request):
    results = Menu.objects.all()
    try:
        data = {
            "menu": results
        }
        return render(request, "menu.html", context=data)
    except:
        return HttpResponseNotFound(request, "../templates/pageNotFound404.html", status=404)
