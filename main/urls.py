from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,re_path
import main.views as main
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView


urlpatterns = [
    path('', main.index, name="main_url"),
    path('main/login/', main.LoginPage.as_view(),name='login'),
    path('main/register/', main.RegisterUser.as_view(), name="register"),
    #path('main/menu/',main.menu, name='menu'),
    # path('main/login/password-change/', PasswordChangeView.as_view(),name="password_change")
    # path('main/login/password-change/password-change-done',PasswordChangeDoneView.as_view(),name="password_change_done")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)