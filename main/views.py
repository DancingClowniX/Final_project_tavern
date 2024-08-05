from django.shortcuts import render, redirect
from feedback.forms import AddFeedbackForm
from .models import Menu, Category,News
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginUserForm
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from .forms import ProfileUserForm
from feedback.models import Feedback
from shop.models import Cart, CartItem
from shop.views import ShopPage
from main.forms import UserPasswordChangeForm
from django.contrib.auth.models import User
from main.models import Tournament


def index(request):
    try:
        cart = Cart.objects.get(user=request.user)
        context = {
            'cart': cart,
        }
        return render(request, "main_page.html", context)
    except:
        return render(request, "main_page.html")



def menu(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    try:
        cart = Cart.objects.get(user=request.user)
        data = {
            "menu": menu,
            "category": category,
            'cart': cart,
        }
        return render(request, "menu.html", context=data)
    except:
        data = {
            "menu": menu,
            "category": category,
        }
        return render(request, "menu.html", context=data)


class PageTemplate(TemplateView):
    template_name = 'meeting.html'
    news_obj = News.objects.all
    extra_context = {
         'news': news_obj,
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            cart = Cart.objects.get(user=self.request.user)
            context['cart'] = cart
        except Cart.DoesNotExist:
            cart = None
            context['cart'] = cart
            return context
        finally:
            return context


def showCategory(request, category_id):
    cat_obj = get_object_or_404(Category, id=category_id)
    menu_items = cat_obj.menu_set.all()
    data = {
        'category': cat_obj,
        'menu_items': menu_items,
    }
    try:
        cart = Cart.objects.get(user=request.user)
        data['cart'] = cart
        return render(request, 'food.html', context=data)
    except Cart.DoesNotExist:
        return render(request, 'food.html', context=data)
    finally:
        return render(request, 'food.html', context=data)


def showFood(request, eat_id):
    menu_obj = get_object_or_404(Menu, id=eat_id)
    feedback_list = Feedback.objects.filter(food=eat_id)

    if request.method == 'POST':
        if 'delete' in request.POST:
            fb_id = request.POST.get('fb_id')
            fb = get_object_or_404(Feedback, id=fb_id)
            if fb.user == request.user or request.user.is_staff:
                fb.delete()
                return redirect('show_food', eat_id=eat_id)

        else:
            form = AddFeedbackForm(request.POST)
            if form.is_valid():
                feedback_instance = form.save(commit=False)
                feedback_instance.food = menu_obj.id
                feedback_instance.user = request.user
                feedback_instance.save()
                return redirect('show_food', eat_id=eat_id)
    else:
        form = AddFeedbackForm()
        data = {
            'food': menu_obj,
            'feedback': feedback_list,
            'add_feedback_form': form,
        }
    try:
        cart = Cart.objects.get(user=request.user)
        data['cart'] = cart
        return render(request, 'food_item.html', context=data)
    except Cart.DoesNotExist:
        return render(request, 'food_item.html', context=data)
    finally:
        return render(request, 'food_item.html', context=data)


class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': "Авторизация", 'form': form_class}

    def get_success_url(self):
        return reverse_lazy('main_url') # перенаправляет на имя по адрессу ПРОверьте setting.py


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('login')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('main_url')


class LoginPage(LoginView):
    form_class = LoginUserForm
    template_name = '../templates/login.html'
    extra_context = {"title":'Авторизация','form':form_class}

    def get_success_url(self):
        return reverse_lazy('main_url') #Settings py


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_url'))


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()  # Используем модель пользователя
    form_class = ProfileUserForm  # Форма профиля пользователя
    template_name = 'profile.html'  # Шаблон для профиля пользователя
    extra_context = {'title': "Профиль пользователя"} #'default_image': settings.DEFAULT_USER_IMAGE}

    # Метод для получения URL после успешного обновления профиля
    def get_success_url(self):
        return reverse_lazy('profile')

    # Метод для получения объекта текущего пользователя
    def get_object(self, queryset=None):
        return self.request.user

def privacy(request):
    return render(request, 'privacy.html')
def contacts(request):
    return render(request, 'contacts.html')
class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'password_change_form.html'
    extra_context = {'title': "Изменение пароля"}

    def get_success_url(self):
        return reverse_lazy('password_change_done')



