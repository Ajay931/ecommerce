from django.shortcuts import render,redirect
from . models import products
from cart.models import item
# Create your views here.

def home(request):
    p1 = products.objects.all()
    return render(request,'index.html',{'prod':p1})


def carts(request):
    if request.method=='POST':
        #itemname = request.POST['item']
        name=request.POST['userid']
        itemobj=products.objects.get(id=name)
        itemname=itemobj.name
        curr_user = request.user
        instance = item.objects.get(username=curr_user)
        instance.pro3=instance.pro2
        instance.pro2=instance.pro1
        instance.pro1=itemname
        instance.save()
        return redirect('/')
    else:
        return render(request,'index.html')

