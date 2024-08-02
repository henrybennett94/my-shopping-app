from django.shortcuts import render
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
        if request.POST.get("new_list"):
            list_name = request.POST.get("list_name")
@login_required(login_url='/login/')
def open_shopping_list(request, list_name):
    queryset = List.objects.filter(status=1)
    list = get_object_or404(queryset, list_name=list_name)
    return render(
        request,
        "lists/templates/lists/shopping_list.html",
        {"list": list},
    )

