from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
# Create your views here.


class orderCreateView(TemplateView):
    template_name = 'orders/order_create.html'

