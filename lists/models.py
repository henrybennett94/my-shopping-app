from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Items(models.Model):
    label = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.label

class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    shop_list = models.CharField(max_length=100, blank=True, null=True)
    shop_item = models.CharField(max_length=100)
    created_on = models.DateTimeField('created on', auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shop_list} {self.created_on}"
