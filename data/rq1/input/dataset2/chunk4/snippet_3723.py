#Source: https://stackoverflow.com/questions/56553165/how-to-fix-typeerror-catg-id-is-an-invalid-keyword-argument
from categories.models import Catg, Type, Product, Choice
from django.shortcuts import render

def ch(request, Type_id, Product_id, Catg_id):
    ca = Catg.objects.get(pk=Catg_id)
    p = Type.objects.get(pk=Type_id)
    cho = Product.objects.get(pk=Product_id)
    alls = Choice.objects.all()
    context3 = {
        'p': p,
        'alls': alls,
        'cho': cho,
        'ca': ca,
    }
    return render(request, "service providers.html", context3)