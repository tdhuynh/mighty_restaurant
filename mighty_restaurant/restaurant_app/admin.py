from django.contrib import admin
from restaurant_app.models import Profile, Item, Table, Order

admin.site.register([Profile, Item, Table, Order])
