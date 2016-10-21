from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from restaurant_app.models import Order, Profile, Table, Item
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


class HomeView(ListView):
    template_name = "home.html"
    model = Table


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("profile_update_view")


class OrderCreateView(CreateView):
    model = Order
    fields = ('item', 'notes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order"] = Order.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.table = Table.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('table_detail_view', args=[int(self.kwargs['pk'])])


class OrderUpdateView(UpdateView):
    model = Order
    success_url = reverse_lazy('table_create_view')
    fields = ('item', 'notes')


class ProfileUpdateView(UpdateView):
    template_name = 'profile.html'
    fields = ('access_level',)
    success_url = reverse_lazy('home_view')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.profile.access_level == 'o' or request.user.profile.access_level == 's' or request.user.profile.access_level == 'c':
    #         return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)
    #     else:
    #         raise PermissionDenied # HTTP 403


class TableCreateView(CreateView):
    model = Table
    fields = ('paid',)
    success_url = reverse_lazy("table_create_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["table_list"] = Table.objects.all()
        return context

class TableDetailView(DetailView):
    model = Table

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_list"] = Order.objects.all()
        return context


class CookDetailView(DetailView):
    model = Order



class CookUpdateView(UpdateView):
    model = Order
    fields = ("completed",)

    def get_success_url(self, **kwargs):
        return reverse_lazy('cook_detail_view', args=[int(self.kwargs['pk'])])

    # def get_object(self):
    #     if  self.request.user.profile.is_cook:
    #         return Order.objects.get(user=self.request.user)
    #
    # def get_queryset(self):
    #     if  self.request.user.profile.is_cook:
    #         return Order.objects.all()

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.user = self.request.user
    #     # instance.order = Order.objects.get(id=self.kwargs['pk'])
    #     return super().form_valid(form)
