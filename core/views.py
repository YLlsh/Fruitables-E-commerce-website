from django.shortcuts import render
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


def vegi(request,id):

    id = id

    obj1 = Vegetables.objects.filter(id=id)
    obj2 = Fruits.objects.all()

    obj2.product_name = obj1.product_name
    obj2.price = obj1.price

    if request.method == "POST":
        plues = request.POST.get('plues')
        minos = request.POST.get('minos')

        if plues:
            q =+1
        elif minos:
            q =- 1
                
    
    obj2.total = obj2.prce * q

    return render(request,"cart.html")
