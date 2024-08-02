from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

#class HomePage(TemplateView):
#    Displays home page" """
#    template_name = 'index.html'

def shopping_list_view(request):
    return render(request, 'shopping_list.html', {'items': GroceryItem.all()})


