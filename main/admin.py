from django.contrib import admin
from .models import News,Menu,Category
# Зарегистрированы модели Новостей/турнира, Меню, Категорий
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'text')
    list_display_links = ('id',)



@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'text', 'price')
    list_display_links = ('id',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id',)
