from django.shortcuts import render , redirect
import products.models as product_model
import cart.models as cart_model
from django.core.paginator import Paginator

from django.http import JsonResponse
# def index(request):
    # return render (request, "core/index.html")


def index(request):
      # Paginator VIEW
    vegetable_objects = product_model.Vegetables.objects.all()
    paginator = Paginator(vegetable_objects, 4)  # 4 items per page
    page_number = request.GET.get('page')
    vege_pag = paginator.get_page(page_number)
    # END Paginator



    # search_bar view 
    query = request.GET.get('q')
    result = []

    if query:
        result = product_model.Vegetables.objects.filter(product_name__icontains=query)
        response =  render(request, "core/index.html",{'results': result, 'query': query})
        return response
    # end search_bar view 

  
    fruits = product_model.Fruits.objects.all()
    Vegetables = product_model.Vegetables.objects.all()

    
    return render(request, 'core/index.html', {'page_obj': vege_pag, 'fruits':fruits, 'Vegetables':Vegetables})


def fruit_to_cart(request,id):
    id = id

    obj1 = product_model.Fruits.objects.get(id=id)

    cart_model.Cart.objects.create(
        product_name = obj1.product_name,
        price = obj1.price,
        )
    
    return redirect("/")

def vegetable_to_cart(request,id):
    id = id

    obj1 = product_model.Fruits.objects.get(id=id)

    cart_model.Cart.objects.create(
        product_name = obj1.product_name,
        price = obj1.price,
        )
    
    return redirect("/")



def suggest_products(request):
    query = request.GET.get('q', '')
    if query:
        results = product_model.Vegetables.objects.filter(product_name__icontains=query)[:5]
        data = [{'product_name': p.product_name, 'price': str(p.price)} for p in results]
        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)