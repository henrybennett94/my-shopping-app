from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    list_name = models.CharField("Your Shopping List", max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField("created on", auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.list_name

class Items(models.Model):
    label = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    list = models.ForeignKey(List, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.label


