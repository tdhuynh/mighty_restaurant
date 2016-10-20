from django.contrib import admin
from restaurant_app.models import Employee, Item, Table, Order

admin.site.register([Employee, Item, Table, Order])
