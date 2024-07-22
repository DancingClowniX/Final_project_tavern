from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class Goods(models.Model):
    title = models.CharField(max_length=150,blank=True, null=True)
    image = models.ImageField(upload_to="goods_image/", blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

class CartItem(models.Model):
    product = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())