from django.db import models
from django.contrib.auth.models import User
from shop.models import Cart


class Order(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    orderItems = models.TextField(verbose_name='Корзина для заказа')
    summa = models.PositiveIntegerField(verbose_name='Сумма заказа', null=True)
    create_order = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    ending_order = models.DateTimeField(verbose_name='Дата завершения заказа', blank=True, null=True)
    is_payment = models.BooleanField(verbose_name='Оплата', default=False)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return str(self.id)


class PaymentStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_payment_complete = models.BooleanField(default=False)


    def __str__(self):
        return f"PaymentStatus(user={self.user.username}, is_payment_complete={self.is_payment_complete})"
