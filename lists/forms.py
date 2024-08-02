from django.forms import ModelForm
from lists.models import List, Items
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm:
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = 'list_name'

class AddItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['label', 'quantity']