from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

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
    access_level = models.CharField(max_length=1, default='s', choices=ACCESS_LEVELS)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    name = models.CharField(max_length=50)
    appetizer = models.BooleanField(default=False)
    entree = models.BooleanField(default=False)
    drink = models.BooleanField(default=False)
    description = models.CharField(max_length=150, null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Table(models.Model):
    paid = models.BooleanField(default=False)

    @property
    def total(self):
        return sum(Order.objects.filter(table=self).filter(Order.item.price))


class Order(models.Model):
    user = models.ForeignKey('auth.User')
    item = models.ForeignKey(Item)
    table = models.ForeignKey(Table)
    notes = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
