from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,re_path,include
import main.views as main
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.views.generic import TemplateView
urlpatterns = [
    path('', main.index, name="main_url"),
    path('main/login/', main.LoginPage.as_view(),name='login'),
    path('main/logout/', main.logout_user, name="logout"),
    path('main/register/', main.RegisterUser.as_view(), name="register"),
    path('main/profile/', main.ProfileUser.as_view(), name="profile"),
    path('main/menu/', main.menu,name="menu"),
    path('main/menu/<int:category_id>', main.showCategory, name='show_cat'),
    path('password-change/', PasswordChangeView.as_view(),name="password_change"),
    path('password-change/password-change-done/',PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('main/meeting/', main.PageTemplate.as_view(),name='meeting'),
]

# urlpatterns = [
#     path('', main.index, name="main_url"),
#     path('main/login/', main.LoginPage.as_view(),name='login'),
#     path('main/logout/', main.LogoutUser.as_view(), name="logout"),
#     path('main/register/', main.RegisterUser.as_view(), name="register"),
#     path('main/profile/', main.ProfileUser.as_view(), name="profile"),
#     path('main/menu/', main.menu,name="menu"),
#     path('main/menu/<str:category>',main.showDrink,name='drinks'),
#     path('password-change/', PasswordChangeView.as_view(),name="password_change"),
#     path('password-change/password-change-done/',PasswordChangeDoneView.as_view(),name="password_change_done"),
#     path('main/meeting/', main.PageTemplate.as_view(),name='meeting'),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)