from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Goods(models.Model):
    title = models.CharField(max_length=150,blank=True, null=True)
    image = models.ImageField(upload_to="goods_image/", blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

class CartItem(models.Model):
    product = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')

    def get_total_price(self):
        return self.product.price * self.quantity
    def get_total_quantity(self):
        return self.quantity

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
    def get_total_quantity(self):
        return sum(item.get_total_quantity() for item in self.items.all())

