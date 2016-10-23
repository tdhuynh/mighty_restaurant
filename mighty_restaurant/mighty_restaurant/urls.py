from django.conf.urls import url, include
from django.contrib import admin
from restaurant_app.views import UserCreateView, OrderCreateView, HomeView, \
                                 ProfileUpdateView, TableCreateView, TableDetailView, \
                                 OrderUpdateView, CookUpdateView, CookListView, \
                                 TableUpdateView, ItemCreateView, ItemUpdateView, \
                                 OrderDeleteView, ItemDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', HomeView.as_view(), name='home_view'),
    url(r'^item/$', ItemCreateView.as_view(), name='item_create_view'),
    url(r'^item/(?P<pk>\d+)/update/$', ItemUpdateView.as_view(), name='item_update_view'),
    url(r'^item/(?P<pk>\d+)/delete/$', ItemDeleteView.as_view(), name='item_delete_view'),
    url(r'^table/(?P<pk>\d+)/order/$', OrderCreateView.as_view(), name='order_create_view'),
    url(r'^order/(?P<pk>\d+)/update$', OrderUpdateView.as_view(), name='order_update_view'),
    url(r'^order/(?P<pk>\d+)/delete$', OrderDeleteView.as_view(), name='order_delete_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^table/$', TableCreateView.as_view(), name='table_create_view'),
    url(r'^table/(?P<pk>\d+)/$', TableDetailView.as_view(), name='table_detail_view'),
    url(r'^table/(?P<pk>\d+)/update_payment$', TableUpdateView.as_view(), name='table_update_view'),
    url(r'^cook/$', CookListView.as_view(), name='cook_list_view'),
    url(r'^cook/(?P<pk>\d+)/complete/$', CookUpdateView.as_view(), name='cook_update_view'),
]
