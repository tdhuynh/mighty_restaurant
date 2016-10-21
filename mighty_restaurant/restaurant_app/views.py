from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from restaurant_app.models import Order


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class OrderCreateView(CreateView):
    model = Order
    success_url = "/"
    fields = ('item', 'table', 'notes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = Order.objects.all()
        return context
