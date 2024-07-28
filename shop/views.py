from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Cart, CartItem
from shop.models import Goods
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin

class ShoppingCart(TemplateView):
    model = get_user_model()  # Используем модель пользователя
    # form_class = ProfileUserForm  # Форма профиля пользователя
    template_name = 'cart.html'  # Шаблон для профиля пользователя
    extra_context = {'title': "Корзина товаров"} #'default_image': settings.DEFAULT_USER_IMAGE}

    # Метод для получения URL после успешного обновления профиля
    def get_success_url(self):
        return reverse_lazy('shop:shop_cart')

    # Метод для получения объекта текущего пользователя
    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            cart = Cart.objects.get(user=self.request.user)
        except Cart.DoesNotExist:
            cart = None
        context['cart'] = cart
        return context


class ShopPage(TemplateView):
    template_name = 'shop.html'
    goods = Goods.objects.all()
    extra_context = {
        'goods': goods,
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получение исходного списка товаров
        products = Goods.objects.all()

        # Количество товаров на странице
        items_per_page = 4

        # Создание объекта Paginator для разбиения списка на страницы
        paginator = Paginator(products, items_per_page)

        # Получение номера страницы из GET-параметра
        page = self.request.GET.get('page')

        try:
            # Получение запрошенной страницы
            product_page = paginator.page(page)

            # Добавление объекта страницы в контекст
            context['product_page'] = product_page

            cart = Cart.objects.get(user=self.request.user)
            context['cart'] = cart
        except PageNotAnInteger:
            # Если номер страницы не является целым числом, отображаем первую страницу
            product_page = paginator.page(1)

            # Добавление объекта первой страницы в контекст
            context['product_page'] = product_page

            cart = Cart.objects.get(user=self.request.user)
            context['cart'] = cart
        except EmptyPage:
            # Если номер страницы находится за пределами диапазона, отображаем последнюю страницу
            product_page = paginator.page(paginator.num_pages)

            # Добавление объекта последней страницы в контекст
            context['product_page'] = product_page

            cart = Cart.objects.get(user=self.request.user)
            context['cart'] = cart
            return context
        finally:
            return context

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Goods, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:shop_cart')


@login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect('shop:shop_cart')


@login_required
def increase(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:shop_cart')

@login_required
def decrease(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    if cart_item.quantity == 1:
        cart_item.delete()
    else:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('shop:shop_cart')