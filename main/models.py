from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150,blank=True, null=True)
    text = models.CharField(max_length=150,blank=True, null=True)
    image = models.ImageField(upload_to="news_image/",blank=True, null=True)


class Menu(models.Model):
    title = models.CharField(max_length=150,verbose_name='Название',blank=True, null=True)
    text = models.CharField(max_length=150,verbose_name='Описание',blank=True, null=True)
    image = models.ImageField(upload_to="menu/image",blank=True, null=True,verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена',blank=True, null=True)