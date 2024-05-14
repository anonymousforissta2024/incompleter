#Source: https://stackoverflow.com/questions/68812247/why-does-error-attribute-error-module-myapp-views-has-no-attribute-symbol-o
from django.shortcuts import render
from . import sub1
global symbol

def home(request):
    return render(request,"home.html")

def result(request):
    global symbol
    symbol = request.GET['St']
    pred_df= sub1.my_main()
    ans=pred_df.tail().to_html()
    return render(request,"result.html",{"ans":ans})