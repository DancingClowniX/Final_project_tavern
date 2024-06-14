from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150,blank=True, null=True)
    text = models.CharField(max_length=150,blank=True, null=True)
    image = models.ImageField(upload_to="news_image/",blank=True, null=True)
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

class Category(models.Model):
    title = models.CharField(max_length=30,verbose_name='Тип блюда',blank=True, null=True)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.title

class Menu(models.Model):
    title = models.CharField(max_length=150,verbose_name='Название',blank=True, null=True)
    text = models.CharField(max_length=150,verbose_name='Описание',blank=True, null=True)
    image = models.ImageField(upload_to="menu/image",blank=True, null=True,verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена',blank=True, null=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


# class RegistratedPerson(models.Model):
#     name = models.CharField(max_length=128)
#
#     class Meta:
#         verbose_name = 'Зарегестрированные на мероприятие'
#         verbose_name_plural = 'Зарегестрированные на мероприятие'
#     def __str__(self):
#         return self.name
#
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(RegistratedPerson, through='Membership')
#
#     def __str__(self):
#         return self.name
#
# class Membership(models.Model):
#     person = models.ForeignKey(RegistratedPerson, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)