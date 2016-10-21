from django.conf.urls import url, include
from django.contrib import admin
from restaurant_app.views import UserCreateView, OrderCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', OrderCreateView.as_view(), name='order_create_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
]
