#Source: https://stackoverflow.com/questions/62132107/typeerror-item-subject-is-no-iterable
from django.shortcuts import render
from shop.models import Category, Item, Comment
from django.http import HttpResponseRedirect, Http404, HttpResponse

def mainpage(request):
    categorys = Category.objects.all().order_by('name')
    return render(request, 'shop/mainpage.html', {'categs':categorys})

def items(request, categ_id):
    try:
        itemss = Item.objects.get(id = categ_id)
    except:
        raise Http404("Not found")

    return render(request, 'shop/items.html', {'itemss':itemss})

def info(request, item_id):
    try:
        item = Item.objects.get(id = item_id)
    except:
        raise Http404("No one item is no found")

    return render(request, 'shop/info.html', {"item":item})