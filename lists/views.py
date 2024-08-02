from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import List, Items
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

#class HomePage(TemplateView):
#    Displays home page" """
#    template_name = 'index.html'

@login_required(login_url='/login/')
def create_shopping_list(request):
    user = request.user
    if request.method == 'POST':
        list_form = ListForm(request.POST)

        if list_form.is_valid():
            shopping_list = list_form.save(commit=False)
            shopping_list.user = request.user
            shopping_list.save()

            return redirect('shopping_list.html', id=shopping_list.id)
        
        else:
            list_form=ListForm()
        
        return render(request, 'shopping_list.html', {
            'list_form': list_form
        })

@login_required(login_url='/login/')
def open_shopping_list(request, id):
    shopping_list = get_object_or404(List, id=id)
    items = shopping_list.items.all()
  #  return render(request, "lists/templates/lists/shopping_list.html",{"list": list},)
    return render(request, 'shopping_list.html', {'shopping_list': shopping_list, 'items': items})

@login_required(login_url='/login/')
def add_item(request):
    add_item_form = AddItemForm(request.POST)
    if add_item_form.is_valid():
        item = add_item_form.save(commit=False)
        item.user = request.user
        item.list = shopping_list
        item.save()

        return redirect('shopping_list.html', id=shopping_list.id)
    
    else:
        add_item_form = AddItemForm()
    
    return render(request, 'shopping_list.html', {
        'add_item_form': add_item_form
    })
