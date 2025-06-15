from django.shortcuts import render , redirect
import products.models as product_model
import cart.models as cart_model
from django.core.paginator import Paginator
import random
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/account/sign_in/")
def index(request):
    # Paginator VIEW
    vegetable_objects = product_model.Vegetables.objects.all()
    paginator = Paginator(vegetable_objects, 4)  # 4 items per page
    page_number = request.GET.get('page')
    vege_pag = paginator.get_page(page_number)
    # end Paginator



    # search_bar view 
    query = request.GET.get('q')
    result = []

    
    if query:
        result = product_model.Vegetables.objects.filter(product_name__icontains=query)
        if result:
            for r in result:
                r.type = "veg"
            response =  render(request, "core/index.html",{'results': result, 'query': query})
        else:
            result = product_model.Fruits.objects.filter(product_name__icontains=query)
            for f in result:
                f.type = "fruit"
            response =  render(request, "core/index.html",{'results': result, 'query': query})

        return response
    # end search_bar view 

   
    fruits = product_model.Fruits.objects.all()
    Vegetables = product_model.Vegetables.objects.all()
    Vegetables_bestSeller = product_model.Vegetables.objects.all()[2:5]

    
    return render(request, 'core/index.html', {'page_obj': vege_pag, 'fruits':fruits, 'Vegetables':Vegetables, "Vegetables_bestSeller":Vegetables_bestSeller})

@login_required(login_url="/account/sign_in/")
def shop_random(request):
    # for random product
    Random_obj = []

    fruit_list = product_model.Fruits.objects.all()
    for f in fruit_list:
        f.type = "fruit"
        Random_obj.append(f)

    veg_list = product_model.Vegetables.objects.all()
    for g in veg_list:
        g.type = "veg"
        Random_obj.append(g)

    obj = random.sample(Random_obj,  min(9, len(Random_obj)))
    # end random product

    # in range seach 
    use_range = request.GET.get('rangeInput')
    if use_range != None:
        use_range = int(use_range)
        all_product = []
        in_range_product = []
        
        obj1 = product_model.Fruits.objects.all()
        for f in obj1:
            f.type = "fruit"
            all_product.append(f)

        obj2 = product_model.Vegetables.objects.all()
        for g in obj2:
            g.type = "veg"
            all_product.append(g)

        for r in all_product:
            if r.price <= use_range:
                in_range_product.append(r)
    
    # end in range serach
        context = {
            'final_result':in_range_product}
        return render(request, "core/shop.html",context)

    return render(request, "core/shop.html",{'shop_Random_choices': obj} )

@login_required(login_url="/account/sign_in/")
def product_random(request):
    Random_obj = []

    fruit_list = product_model.Fruits.objects.all()
    for f in fruit_list:
        f.category = "Fruits"
        Random_obj.append(f)

    veg_list = product_model.Vegetables.objects.all()
    for g in veg_list:
        g.category = "Vegetables"
        Random_obj.append(g)
    obj = random.sample(Random_obj,  min(1, len(Random_obj)))

    obj1 = product_model.Fruits.objects.all()
    obj2 =product_model.Vegetables.objects.all()

    return render(request, "core/product_detail.html", {'Random_choicess': obj, 'obj1':obj1, 'obj2':obj2})


@login_required(login_url="/account/sign_in/")
def fruit_to_cart(request,id, path):
    id = id
    obj1 = product_model.Fruits.objects.get(id=id)

    cart_model.Cart.objects.create(
        user = request.user,
        product_name = obj1.product_name,
        price = obj1.price,
        )
    if path == '/shop/':
        return redirect("/shop/")
    elif path == '/product_detail/':
        return redirect("/product_detail/")

    return redirect("/")
@login_required(login_url="/account/sign_in/")
def vegetable_to_cart(request, id, path):
    id = id
    obj1 = product_model.Vegetables.objects.get(id=id)

    cart_model.Cart.objects.create(
        user = request.user,
        product_name = obj1.product_name,
        price = obj1.price,
        )
    if path == '/shop/':
         return redirect("/shop/")
    elif path == '/product_detail/':
        return redirect("/product_detail/")

    return redirect("/")

@login_required(login_url="/account/sign_in/")
def suggest_products(request):
    query = request.GET.get('q', '')
    if query:
        results = product_model.Vegetables.objects.filter(product_name__icontains=query)[:5]
        if results:
            data = [{'product_name': p.product_name, 'price': str(p.price)} for p in results]
        else:
            results = product_model.Fruits.objects.filter(product_name__icontains=query)[:5]
            data = [{'product_name': p.product_name, 'price': str(p.price)} for p in results]

        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)
@login_required(login_url="/account/sign_in/")
def search_result(request,id, type):
     # search result to shop detail

    all_product = []
    
    obj1 = product_model.Fruits.objects.all()
    for f in obj1:
        f.type = "fruit"
        all_product.append(f)

    obj2 = product_model.Vegetables.objects.all()
    for g in obj2:
        g.type = "veg"
        all_product.append(g)
    id = id 

    for result in all_product:
        if id == result.id and type == result.type:
            final_result = result
    
    return render(request, "core/product_detail.html",{'final_result':final_result})

@login_required(login_url="/account/sign_in/")
def product_range(request):
    range = request.GET.get('rangeInput')
    
    all_product = []
    in_range_product = []
    
    obj1 = product_model.Fruits.objects.all()
    for f in obj1:
        f.type = "fruit"
        all_product.append(f)

    obj2 = product_model.Fruits.objects.all()
    for g in obj2:
        g.type = "veg"
        all_product.append(g)

    for r in all_product:
        if range <= r.price:
            in_range_product = r

    return render(request, "core/shop.html",{'final_result':in_range_product})
