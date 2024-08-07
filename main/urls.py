from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
import main.views as main
from django.contrib.auth.views import PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

app_name = 'main'

urlpatterns = [
    path('', main.index, name="main_url"), # <--- HomePage

    # Авторизация/регистрация 🔽
    path('main/login/', main.LoginPage.as_view(),name='login'),
    path('main/logout/', main.logout_user, name="logout"),
    path('main/register/', main.RegisterUser.as_view(), name="register"),
    path('main/profile/', main.ProfileUser.as_view(), name="profile"),
    path('password-change/', main.UserPasswordChange.as_view(), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name="password_change_done"),


    # Остальное 🔽
    path('main/menu/', main.menu, name="menu"),
    path('main/menu/category/<int:category_id>', main.showCategory, name='show_cat'),
    path('main/meeting/', main.PageTemplate.as_view(),name='meeting'),
    path('main/menu/<int:eat_id>', main.showFood,name='show_food'),
    path('main/privacy/', main.privacy,name='privacy'),
    path('main/contacts/', main.contacts,name='contacts'),
    path('main/meeting/', main.PageTemplate.as_view(),name='get_tournament_users')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)