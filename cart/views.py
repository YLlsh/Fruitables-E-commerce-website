from django.shortcuts import render, redirect, get_object_or_404
from .models import * 
from django.db.models import Q,Sum
# Create your views here.

def cart(request):
    obj = Cart.objects.all()

    total = Cart.objects.aggregate(
        total=Sum('total',filter=Q(total__isnull=False)))
    
    t = total['total']
    return render(request,"core/cart.html",{'carts':obj,'total':t} )

def cart_modify_minos(request, m):
    obj = get_object_or_404(Cart, id=m)
    
    if obj.quantity > 1:
        obj.quantity -= 1
        obj.save()
    
    return redirect("cart")

def cart_modify_plus(request, p):
    obj = get_object_or_404(Cart, id=p)
    obj.quantity += 1
    obj.save()
    
    return redirect("cart")

def cart_delete(request, d):

    obj = get_object_or_404(Cart, id=d)

    obj.delete()

    return redirect("cart")