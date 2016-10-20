from django.db import models

ACCESS_LEVELS = [
    ('o','owner'),
    ('s','server'),
    ('c','cook'),
]

class Employee(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, default='s', choices=ACCESS_LEVELS)

class Item(models.Model):
    name = models.CharField(max_length=50)
    appetizer = models.BooleanField(default=False)
    entree = models.BooleanField(default=False)
    drink = models.BooleanField(default=False)
    description = models.CharField(max_length=150)
    price = models.FloatField()

class Table(models.Model):
    paid = models.BooleanField(default=False)

    @property
    def total(self):
        return sum(Order.objects.filter(table=self).filter(item.price))


class Order(models.Model):
    user = models.ForeignKey('auth.User')
    item = models.ForeignKey(Item)
    table = models.ForeignKey(Table)
    notes = models.TextField()
    completed = models.BooleanField(default=False)
