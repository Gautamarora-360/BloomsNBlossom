from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact, Order, OrderUpdate
from math import ceil
import json


def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nslides, 'range':range(1, nslides), 'product':products}
    # allProducts = [[products, range(1, nslides), nslides],
    #                [products, range(1, nslides), nslides]]
    # params = {'allProducts' : allProducts}
    # return render(request, 'shop/index.html', params)

    # -- Sahi wala
    allProducts = []
    categProducts = Product.objects.values('category', 'id')
    categs = {item['category'] for item in categProducts}
    for cat in categs:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allProducts.append([prod, range(1, nslides), nslides])
    params = {'allProducts':allProducts}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    if query in item.description.lower() or query in item.category.lower() or query in item.sub_category.lower() or query in item.product_name.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    query = query.lower()
    allProducts = []
    categProducts = Product.objects.values('category', 'id')
    categs = {item['category'] for item in categProducts}
    for cat in categs:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProducts.append([prod, range(1, nslides), nslides])
    params = {'allProducts': allProducts, 'msg': ""}
    if len(allProducts) == 0 or len(query) < 3:
        params = {'msg': "No results matched the entered query!"}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
        return render(request, 'shop/thanks_for_contacting.html')
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "noitem"}')
        except Exception as e:
            return HttpResponse('{"status": "error"}')
    return render(request, 'shop/tracker.html')


def productview(request, myID):
    product = Product.objects.filter(id=myID)
    print(product)
    return render(request, 'shop/productview.html', {'product': product[0]})


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(items_json=items_json, name=name, email=email, phone=phone, address=address, city=city, state=city, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')