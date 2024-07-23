from django.contrib import admin
from .models import Goods,CartItem,Goods

# Register your models here.
@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'price')
    list_display_links = ('id',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'cart')
    list_display_links = ('id',)