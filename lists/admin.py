from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.List)
admin.site.register(models.Items)
admin.site.register(models.ShoppingList)