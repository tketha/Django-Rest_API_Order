from django.db import models


class Order(models.Model):
    itemid = models.IntegerField()
    itemname = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.itemname

