from django.shortcuts import render, redirect
from .models import Products, Categories
from random import randint
from datetime import datetime

def index(request):
    produtos = Products.objects.all()
    for produto in produtos:
        print(produto.name)
    return render(request, 'pages/index.html', {'produtos':produtos})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = randint(100, 10000)
        category = request.POST.get('category')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        description = request.POST.get('description')
        qtd = request.POST.get('qtd')
        discount = request.POST.get('discount')
        created_at = datetime.now()
        in_stock = True

        Products.objects.create(
            name = name,
            cod = code,
            category_id = category,
            image = image,
            price = price,
            description = description,
            qtd = qtd,
            discount = discount,
            created_at = created_at,
            in_stock = in_stock
        )
        return redirect('home')
    else:
        categories = Categories.objects.all()
        return render(request, 'pages/add-product.html', {'categories':categories})
    
def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('home')

def product_details(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'pages/product-details.html', {'product':product})