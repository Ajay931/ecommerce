from django.shortcuts import render,redirect
from .models import item
from layout.models import products

# Create your views here.

def disp(request):
        obj = request.user
        st = obj.username
        p = item.objects.get(username=st)
        item1=p.pro1
        print(item1)
        item2=p.pro2
        item3=p.pro3
        proobj1 = products.objects.get(name=item1)
        proobj2 = products.objects.get(name=item2)
        proobj3 = products.objects.get(name=item3)
        p=[proobj1,proobj2,proobj3]
        return render(request,'carts.html',{'cartitems':p})

def buy(request):
        return render(request,'buy.html')
