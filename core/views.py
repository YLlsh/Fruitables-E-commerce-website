from django.shortcuts import render, redirect
import products.models as product_model
import cart.models as cart_model
from django.core.paginator import Paginator
import random
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# def move_data():
#     fru = product_model.Product.objects.filter(category=2)
#     c = product_model.Category.objects.get(id=2)

#     for i in fru:
#         product_model.Product.objects.create(

#             category = c,
#             product_name = i.product_name,
#             description = i.description,
#             price = i.price,
#             quantity = i.quantity,
#             image = i.image,
#         )

#     return "done"


@login_required(login_url="/account/sign_in/")
def index(request):
    # Paginator VIEW
    vegetable_objects = product_model.Product.objects.filter(category=1)
    paginator = Paginator(vegetable_objects, 4)  # 4 items per page
    page_number = request.GET.get('page')
    vege_pag = paginator.get_page(page_number)
    # end Paginator

    # search_bar view

    # end search_bar view

    fruits = product_model.Product.objects.filter(category=2)
    Vegetables = product_model.Product.objects.filter(category=1)
    Vegetables_bestSeller = product_model.Product.objects.filter(category=1)[
        2:5]

    return render(request, 'core/index.html', {'page_obj': vege_pag, 'fruits': fruits, 'Vegetables': Vegetables, "Vegetables_bestSeller": Vegetables_bestSeller})


def search_suggestions(request):
    query = request.GET.get("q")
    data = []

    if query:
        products = product_model.Product.objects.filter(
            product_name__icontains=query
        )[:5]

        for p in products:
            data.append({
                "id": p.id,
                "name": p.product_name,
                "price": p.price,
                # or p.type if exists
            })

    return JsonResponse(data, safe=False)


@login_required(login_url="/account/sign_in/")
def shop_random(request):
    # for random product
    Random_obj = []

    fruit_list = product_model.Product.objects.filter(category=2)
    for f in fruit_list:
        f.type = "fruit"
        Random_obj.append(f)

    veg_list = product_model.Product.objects.filter(category=1)
    for g in veg_list:
        g.type = "veg"
        Random_obj.append(g)

    obj = random.sample(Random_obj,  min(9, len(Random_obj)))
    # end random product
    all_product = product_model.Product.objects.all()
    # keyword base search 
    keywords = request.GET.get("keywords","")

    if keywords:
        all_product = all_product.filter(product_name__icontains = keywords)

    # in range seach
    use_range = request.GET.get('rangeInput')
 
    if use_range:
        use_range = int(use_range)
        all_product = all_product.filter(price__lt = use_range)

    # end in range serach
        context = {
            'final_result': all_product, 
            'keywords':keywords,
            "use_range": use_range}
        
        return render(request, "core/shop.html", context)

    return render(request, "core/shop.html", {'shop_Random_choices': obj,'final_result':all_product,'keywords':keywords})


@login_required(login_url="/account/sign_in/")
def product_random(request):

    obj = product_model.Product.objects.all().order_by('?')[1]

    obj1 = product_model.Product.objects.filter(
        category=obj.category).order_by('?')[:8]

    return render(request, "core/product_detail.html", {'Random_choicess': obj, 'obj1': obj1})


@login_required(login_url="/account/sign_in/")
def fruit_to_cart(request, id, path):
    id = id
    obj1 = product_model.Fruits.objects.get(id=id)

    cart_model.Cart.objects.create(
        user=request.user,
        product_name=obj1.product_name,
        price=obj1.price,
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
        user=request.user,
        product_name=obj1.product_name,
        price=obj1.price,
    )
    if path == '/shop/':
        return redirect("/shop/")
    elif path == '/product_detail/':
        return redirect("/product_detail/")

    return redirect("/")


@login_required(login_url="/account/sign_in/")
def add_to_cark(request, id):
    product = product_model.Product.objects.get(id=id)

    cart_model.Cart.objects.create(
        user=request.user,
        product=product,
        price=product.price,
    )

    return redirect("/")


@login_required(login_url="/account/sign_in/")
def suggest_products(request):
    query = request.GET.get('q', '')
    if query:
        results = product_model.Vegetables.objects.filter(
            product_name__icontains=query)[:5]
        if results:
            data = [{'product_name': p.product_name,
                     'price': str(p.price)} for p in results]
        else:
            results = product_model.Fruits.objects.filter(
                product_name__icontains=query)[:5]
            data = [{'product_name': p.product_name,
                     'price': str(p.price)} for p in results]

        return JsonResponse(data, safe=False)
    return JsonResponse([], safe=False)


@login_required(login_url="/account/sign_in/")
def search_result(request, id):
    # search result to shop detail

    final_result = product_model.Product.objects.filter(id=id).first()

    return render(request, "core/product_detail.html", {'final_result': final_result})


# @login_required(login_url="/account/sign_in/")
# def product_range(request):
#     range = request.GET.get('rangeInput')

#     all_product = []
#     in_range_product = []

#     obj1 = product_model.Product.objects.filter(category=2)
#     for f in obj1:
#         f.type = "fruit"
#         all_product.append(f)

#     obj2 = product_model.Product.objects.filter(category=2)
#     for g in obj2:
#         g.type = "veg"
#         all_product.append(g)
#     print(range)
#     print(type(range))

#     for r in all_product:
#         if range <= r.price:
#             in_range_product = r

#     return render(request, "core/shop.html", {'final_result': in_range_product,"range":range})
