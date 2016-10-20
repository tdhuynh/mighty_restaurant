from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"
