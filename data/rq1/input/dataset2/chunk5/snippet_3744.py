#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from django.shortcuts import redirect, render
# from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get()
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')