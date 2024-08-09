from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginUserForm
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .forms import ProfileUserForm

from main.views import index
from django.test import TransactionTestCase

# Написан тест (не функционален)
def test_views_correct_template(self):
    '''URL-адрес использует соответствующий шаблон.'''
    templates_url_names = {
        reverse('posts:index'): 'posts/index.html',
        reverse('posts:group_list',
                kwargs={'slug':
                            f'{self.group.slug}'}): 'posts/group_list.html',
        reverse('posts:profile',
                kwargs={'username':
                            f'{self.user.username}'}): 'posts/profile.html',
        reverse('posts:post_detail',
                kwargs={'post_id':
                            self.post.id}): 'posts/post_detail.html',
        reverse('posts:post_create'): 'posts/create_post.html',
        reverse('posts:post_edit',
                kwargs={'post_id':
                            self.post.id}): 'posts/create_post.html'}
    for adress, template in templates_url_names.items():
        with self.subTest(adress=adress):
            response = self.authorized_client.get(adress)
            error_name = f'Ошибка: {adress} ожидал шаблон {template}'
            self.assertTemplateUsed(response, template, error_name)