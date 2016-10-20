from django.conf.urls import url, include
from django.contrib import admin
from restaurant_app.views import UserCreateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', UserCreateView.as_view(), name='user_create_view'),
]
