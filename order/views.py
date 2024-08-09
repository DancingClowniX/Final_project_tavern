import uuid
from django.shortcuts import Http404,HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.views.generic import TemplateView, ListView, DetailView, View
from shop.models import Cart, CartItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from yookassa import Payment, Configuration
import json
from django.views.decorators.csrf import csrf_exempt
from .models import PaymentStatus
from order.models import Order
from shop.models import Goods
from django.contrib.auth.models import User
import datetime
from django.contrib.contenttypes.models import ContentType
import requests

# Данные для Ю-касса для связи с сайтом
Configuration.account_id = "433859"
Configuration.secret_key = "test_HOkl1FeKmf7MzVWittmOSNsTX_Ds2izw8oPz92Ly6mI"

# Функция добавления платежа на Юкасса
def add_payment(price, title, meta):
    payment_id = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://dancingclownix.pythonanywhere.com/shop/cart/"
        },
        "capture": True,
        "description": title,
        "metadata": meta
    }, payment_id)
    return payment

# Функция оплаты товара
@login_required
def cart_pay(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    total_price = cart.get_total_price()
    total_items = cart.items.count()

    meta = {
        "user_id": request.user.id,
    }

    try:
        payment = add_payment(total_price, f'Худи: {total_items}', meta)
    except Exception as e:
        return redirect('shop:shop_cart')

    return redirect(payment.confirmation.confirmation_url)

# Функция отправки в tg bot данных
def send_telegram_message(text):
    token = '7295540178:AAF9W6cL5XKLf1M6dKXCGk1nt5jaAUkmGl0'
    chat_id = '755109015'
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    return response.json()

# Функция обработки платежа и обращения к api telegramm
@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)

        payment_object = payload['object']
        user_id = int(payment_object['metadata']['user_id'])
        user = get_object_or_404(User, id=user_id)
        status = payment_object['status']

        if status == 'succeeded':
            payment_status, created = PaymentStatus.objects.get_or_create(user=user)
            payment_status.is_payment_complete = True
            payment_status.save()

            cart = get_object_or_404(Cart, user=user)
            orderItems = ''

            for cart_item in cart.items.all():
                product = get_object_or_404(Goods, id=cart_item.product.id)
                quantity = cart_item.quantity
                orderItems += f'{product.title} - {quantity}шт., '
                product.quantity -= quantity
                product.save()

            sum_ = float(payment_object['amount']['value'])
            message = f"Пользователь {user.username}, {user.email} произвел оплату мерча: {orderItems} на сумму: {sum_}"
            Order.objects.create(user=user, orderItems=orderItems, summa=sum_, is_payment=True)
            cart.items.all().delete()
            try:
                send_telegram_message(message)
            except Exception:
                pass

            return HttpResponse(status=200)
        else:
            return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


