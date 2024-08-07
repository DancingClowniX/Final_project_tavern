from django.contrib import admin
from order.models import Order
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'orderItems', 'summa', 'create_order', 'ending_order',)
    list_display_links = ('id',)

    def cart(self, obj):
        return ", ".join([str(related) for related in obj.related_field.all()])

    cart.short_description = 'Related Field'