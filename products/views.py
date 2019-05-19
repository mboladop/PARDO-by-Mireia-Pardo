from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product, Category
from django.http import HttpResponse

def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})

def category_detail(request, pk):
    products = get_list_or_404(Product, category=pk)
    return render(request, 'products/products.html', {"products": products, "current": int(pk)})


def product_profile(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_profile.html", {'product': product})
    
def search(request):
    products = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "products/products.html", {"products": products})

