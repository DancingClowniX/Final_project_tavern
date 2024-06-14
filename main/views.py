from django.shortcuts import render
from .models import News
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.exceptions import ValidationError
from main.forms import LoginUserForm,User,UserCreationForm,AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import RegisterUserForm,ProfileUserForm
from .models import Menu, Category
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from shop.views import ShopPage
from feedback.models import Feedback

# Create your views here.
def index(request):
    #results = News.objects.all()
        #data = {
        #    "news": results
        #}
    return render(request, "main_page.html") #context=data)
    # except:
    #     return HttpResponseNotFound(request, "pageNotFound404.html", status=404)



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

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_url'))





# Класс ProfileUser для отображения и редактирования профиля пользователя
class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()  # Используем модель пользователя
    form_class = ProfileUserForm  # Форма профиля пользователя
    template_name = 'profile.html'  # Шаблон для профиля пользователя
    extra_context = {'title': "Профиль пользователя"}# 'default_image': settings.DEFAULT_USER_IMAGE}

    # Метод для получения URL после успешного обновления профиля
    def get_success_url(self):
        return reverse_lazy('profile')

    # Метод для получения объекта текущего пользователя
    def get_object(self, queryset=None):
        return self.request.user

def menu(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    data = {
    "menu": menu,
    "category": category
    }
    return render(request, "menu.html", context=data)


class PageTemplate(TemplateView):
    template_name = 'meeting.html'
    extra_context = {
         'name': 'Template_View страница',
         #'menu': menu,
         #'posts': Post.objects.all() #Women.published.all().select_related('cat'),
    }
def showCategory(request, category_id):
    cat_obj = get_object_or_404(Category, id=category_id)
    menu_items = cat_obj.menu_set.all()
    data = {
        'category': cat_obj,
        'menu_items': menu_items
    }
    return render(request, 'food.html', context=data)

def showFood(request,title):
    menu_obj = get_object_or_404(Menu, title=title)
    data = {
        'food': menu_obj
    }
    return render(request,'food_item.html',context=data)

class Food_Detail(DetailView):
    model = Menu
    template_name = 'food_item.html'
    context_object_name = 'food'
    pk_url_kwarg = 'food_id'  # Имя переменной в URL для первичного ключа

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Menu.objects.get(id=self.kwargs['food_id']) # заменить
        feedbacks = product.feedback_set.all()
        context['feedbacks'] = feedbacks
        return  context