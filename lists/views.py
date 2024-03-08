from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Item, List

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    # return render(request, 'list.html', {
    #     'items': List.objects.get(id=list_id).items
    # })
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
