from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,re_path,include
import order.views as order
from django.views.generic import TemplateView

app_name = 'order'

urlpatterns = [
    path('cart_pay/<int:cart_id>/', order.cart_pay, name='cart_pay'),
    path('webhook/', order.webhook, name='webhook'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)