from django.shortcuts import render , redirect
from products.models import *
from django.core.paginator import Paginator
from cart.models import *
# def index(request):
    # return render (request, "core/index.html")


def index(request):
    vegetable_objects = Vegetables.objects.all()
    paginator = Paginator(vegetable_objects, 4)  # 4 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    obj1 = Fruits.objects.all()

    
    return render(request, 'core/index.html', {'page_obj': page_obj, 'fruits':obj1})


def fruit(request,id):
    id = id

    obj1 = Fruits.objects.get(id=id)
    

    Cart.objects.create(
        product_name = obj1.product_name,
        price = obj1.price,
        )
    
    return redirect("/")
