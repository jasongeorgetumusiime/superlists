from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Item, List

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list/')

def view_list(request):
    return render(request, 'list.html', {'items': Item.objects.all()})
