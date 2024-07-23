from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include
from shop import views as shop



app_name = 'shop'

urlpatterns = [
    path('', shop.ShopPage.as_view(), name='shop_page'),
    path('cart/', shop.ShoppingCart.as_view(), name='shop_cart'),
    path('add/<int:product_id>/', shop.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', shop.remove_from_cart, name='remove_from_cart'),
    path('increase/<int:product_id>/', shop.increase, name='increase'),
    path('decrease/<int:product_id>/', shop.decrease, name='decrease'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)