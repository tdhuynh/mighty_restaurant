from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class ItemCreateView(CreateView):
    model = Item
    fields = ('name', 'group', 'description', 'price')
    success_url = reverse_lazy('item_create_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_list"] = Item.objects.all()
        return context

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return Item.objects.all()
        raise Exception("YOU CAN'T BE HERE")


class ItemUpdateView(UpdateView):
    model = Item
    fields = ('name', 'group', 'description', 'price')
    success_url = reverse_lazy('item_create_view')

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return Item.objects.all()
        raise Exception("YOU CAN'T BE HERE")


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('item_create_view')

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return Item.objects.all()
        raise Exception("YOU CAN'T BE HERE")


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

    def get_queryset(self):
        if self.request.user.profile.is_owner or self.request.user.profile.is_server:
            return Order.objects.all()
        raise Exception("YOU CAN'T BE HERE")


class OrderUpdateView(UpdateView):
    model = Order
    success_url = reverse_lazy('table_create_view')
    fields = ('item', 'notes')

    def get_queryset(self):
        if self.request.user.profile.is_owner or self.request.user.profile.is_server:
            return Order.objects.all()
        raise Exception("YOU CAN'T BE HERE")


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('table_create_view')

    def get_queryset(self):
        if self.request.user.profile.is_owner or self.request.user.profile.is_server:
            return Order.objects.all()
        raise Exception("YOU CAN'T BE HERE")


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

    # def get_queryset(self):
    #     if not self.request.user.profile.access_level == 'c':
    #         return Table.objects.all()
    #     raise Exception("YOU CAN'T BE HERE")


class TableDetailView(DetailView):
    model = Table

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_list"] = Order.objects.all()
        return context

    def get_queryset(self):
        if self.request.user.profile.is_owner or self.request.user.profile.is_server:
            return Table.objects.all()
        else:
            raise Exception("You do not have access")
        # return get_queryset


class TableUpdateView(UpdateView):
    model = Table
    success_url = reverse_lazy("table_create_view")
    fields = ('paid',)

    def get_queryset(self):
        if self.request.user.profile.is_owner or self.request.user.profile.is_server:
            return Table.objects.filter(paid=False)


class TableDeleteView(DeleteView):
    model = Table
    success_url = reverse_lazy("table_create_view")

    def get_queryset(self):
        if self.request.user.profile.is_owner or self.request.user.profile.is_server:
            return Table.objects.all()
        raise Exception("YOU CAN'T BE HERE")


class CookListView(ListView):
    template_name = 'cook_order.html'
    model = Order

    def get_queryset(self):
        if self.request.user.profile.is_owner or self.request.user.profile.is_cook:
            return Order.objects.filter(completed=False)
        raise Exception("YOU CAN'T BE HERE")


class CookUpdateView(UpdateView):
    model = Order
    fields = ("completed",)
    success_url = reverse_lazy('cook_list_view')

    def get_queryset(self):
        if self.request.user.profile.is_owner or self.request.user.profile.is_cook:
            return Order.objects.all()
        raise Exception("YOU CAN'T BE HERE")

    # def get_object(self):
    #     if  self.request.user.profile.is_cook:
    #         return Order.objects.get(user=self.request.user)

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.user = self.request.user
    #     # instance.order = Order.objects.get(id=self.kwargs['pk'])
    #     return super().form_valid(form)
