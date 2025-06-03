from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def cart(request):
    obj = Cart.objects.all()
    obj.total()
    return render(request,"core/cart.html",{'carts':obj} )

def cart_modify_minos(m):
    id = m
    obj = Cart.objects.get(id=id)
    quantity = 1
    if m and quantity > 1:
        quantity =-1

    
    obj.total = obj.price * quantity

    return redirect("home/cart")



def cart_modify_plus(p):
    id = p
    quantity = 1
    if p:
        quantity =+1
   

    obj = Cart.objects.get(id=id)
    obj.total = obj.price * quantity

    return redirect("home/cart")