from django.forms import ModelForm
from lists.models import Items, ShoppingList
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm:
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

class ListForm(ModelForm):
    class Meta:
        model = ShoppingList
        fields = "__all__"

"""
class AddItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ('label', 'quantity',)
"""