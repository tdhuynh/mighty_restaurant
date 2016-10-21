from django.conf.urls import url, include
from django.contrib import admin
from restaurant_app.views import UserCreateView, OrderCreateView, HomeView, \
                                 ProfileUpdateView, TableCreateView, TableDetailView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', HomeView.as_view(), name='home_view'),
    url(r'^order/$', OrderCreateView.as_view(), name='order_create_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name='profile_update_view'),
    url(r'^table/$', TableCreateView.as_view(), name='table_create_view'),
    url(r'^table/(?P<pk>\d+)/$', TableDetailView.as_view(), name='table_detail_view'),
]
