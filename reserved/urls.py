from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,re_path,include
import reserved.views as reserved
from django.views.generic import TemplateView

urlpatterns = [
    path('', reserved.reserved_main.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)