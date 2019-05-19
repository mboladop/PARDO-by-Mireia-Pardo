from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product
from .utils import get_cart_items_and_total
# Create your views here.
def see_cart(request):
    cart = request.session.get('cart', [])
    context = get_cart_items_and_total(cart)
    return render(request, "cart/viewcart.html", context)
    
def add_to_cart(request):   
    # Get the product we're adding
    id = request.POST['product_id']
    size = request.POST.get('product_size', 0)
    product = get_object_or_404(Product, pk=id)
    
    # Get the current Cart
    cart = request.session.get('cart', [])
    needsInsert = True
    for c in cart:
        if c['product'] == id and c['size'] == size:
            c['total'] = c['total'] + 1
            needsInsert = False

    # Update the Cart
    if needsInsert:
        cart.append({ "total": 1, "size": size, "product": id})
   
    # Save the Cart back to the session
    request.session['cart'] = cart
    
    # Redirect somewhere
    return redirect('get_products')
    
def remove_from_cart(request):
    # Position of item taken form del_items usin forloop.counter.
     pos = int(request.POST['del_item'])-1
     cart = request.session.get('cart', {})
     if cart[pos]['total']==1:
        del cart[pos]
     # If >1 item in pos it -1
     elif cart[pos]['total']>1:
        cart[pos]['total']-=1
     request.session['cart'] = cart
     return  redirect('see_cart')

def clear(request):
    cart = request.session
    product = Product.objects.all()
    cart.clear()
    return redirect('see_cart')