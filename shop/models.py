from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

# class Goods(models.Model):
#     title = models.CharField(max_length=150,blank=True, null=True)
#     image = models.ImageField(upload_to="goods_image/", blank=True, null=True)
#     price = models.IntegerField()
#
#     class Meta:
#         verbose_name = 'Товары'
#         verbose_name_plural = 'Товары'