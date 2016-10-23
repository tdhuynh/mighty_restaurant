from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Sum



ACCESS_LEVELS = [
    ('o', 'owner'),
    ('s', 'server'),
    ('c', 'cook'),
]

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

    def __str__(self):
        return self.user.username

    @property
    def is_owner(self):
        return self.access_level == 'o'

    @property
    def is_server(self):
        return self.access_level == 's'

    @property
    def is_cook(self):
        return self.access_level == 'c'



GROUP = [
    ('a', 'appetizer'),
    ('e', 'entree'),
    ('b', 'beverage'),
    ('d', 'dessert'),
    ('s', 'side'),
]

class Item(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=1, choices=GROUP)
    description = models.CharField(max_length=150, null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Table(models.Model):
    paid = models.BooleanField()

    def all_orders(self):
        return Order.objects.filter(table=self)

    @property
    def total(self):
        return sum(food.item.price for food in self.all_orders())

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    user = models.ForeignKey('auth.User')
    item = models.ForeignKey(Item)
    table = models.ForeignKey(Table)
    notes = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    # def __str__(self):
    #     return "{} {}".format(self.item.name, self.table.id)

    # def total(self):
    #     return Items.objects.filter(item)
