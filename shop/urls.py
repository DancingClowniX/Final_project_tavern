from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,re_path,include
import shop.views as shop
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.views.generic import TemplateView

urlpatterns = [
    path('', shop.ShopPage.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)