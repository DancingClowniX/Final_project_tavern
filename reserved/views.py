from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from reserved.models import Table

class reserved_main(TemplateView):
    template_name = 'reserved.html'
    table = Table.objects.all()
    extra_context = {
         'table': table,
    }