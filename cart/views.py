from django.shortcuts import render, redirect, get_object_or_404
from .models import * 
from django.db.models import Q,Sum
import checkOut.models as checkout_model 
import cart.models as cart_model 

# Create your views here.

def cart(request):
    obj = cart_model.Cart.objects.all()

    total = cart_model.Cart.objects.aggregate(
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

  # Adjust import as per your project structure

def proceed_checkout(request):
    cart_items = cart_model.Cart.objects.all()

    # Clear old checkouts (optional, if needed per user/session)
    checkout_model.checkOut.objects.all().delete()

    # Move cart items to checkout
    for item in cart_items:
        checkout_model.checkOut.objects.create(
            product_name=item.product_name,
            quantity=item.quantity,
            price=item.price,
            total=item.total
        )

    # Get new checkout data
    checkout_items = checkout_model.checkOut.objects.all()

    total = checkout_model.checkOut.objects.aggregate(
        total=Sum('total',filter=Q(total__isnull=False)))
    sum = total['total']

    return render(request, "core/chackout.html", {'checkouts': checkout_items,'total_sum':sum})
