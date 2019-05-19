from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def get_cart_items_and_total(cart):
    cart_items = []
    total = 0
    total_items = 0
    for p in cart:
        product = get_object_or_404(Product, pk = p['product'] )
        cart_item = {
            'product': product, 
            'quantity': p['total'],
            'size': p['size'],
            'sub_total': p['total']*product.price
        }
        cart_items.append(cart_item)
        total += cart_item['sub_total']
        total_items += p['total']
    return {'cart_items': cart_items, 'total': total, 'total_items': total_items}