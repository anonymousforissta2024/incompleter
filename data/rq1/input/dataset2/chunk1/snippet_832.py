#Source: https://stackoverflow.com/questions/46057819/attribute-error-method-object-has-no-attribute
from django.shortcuts import render
from django.http import Http404

from inventory.models import Item

def index(request):
    items = Item.objects.exclude(aantal=0)
    return render (request, 'inventory/index.html', {
        'items': items,
    })
    return HttpResponse('<p>In index view</p>')

def item_detail(request, id):
    try:
        item = Item.objects.get.id=(id) #THIS ONE CAUSES PROBLEM???
    except Item.DoesNotExist:
        raise Http404('Dit item bestaat niet')
    return render(request, 'inventory/item_detail.html', {
        'item': item,
    })