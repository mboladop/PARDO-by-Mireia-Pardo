from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from django.contrib import messages
from cart.utils import get_cart_items_and_total
from .utils import save_order_items, charge_card, send_confirmation_email
import stripe
from django.conf import settings

# Create your views here.
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)    
        if order_form.is_valid() and request.POST['stripe_id']:
            # Save The Order
            # añadir cargar user id si lo hay
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            # Save the Order Line Items
            cart = request.session.get('cart', {})
            save_order_items(order, cart)
        
            # Charge the Card
            items_and_total = get_cart_items_and_total(cart)
            total = items_and_total['total']
            stripe_token=request.POST['stripe_id']

            try:
                customer = charge_card(stripe_token, total)
            except stripe.error.CardError:
                messages.warning(request, "¡Pago no completado!")

            if customer['paid']:
                messages.success(request, "¡Pago realizado correctamente!")

                # Send Email
                send_confirmation_email(request.POST['email'], request.POST['full_name'], items_and_total)
                send_confirmation_email('pardobymireia@gmail.com', request.POST['full_name'], items_and_total)
        
                #Clear the Cart
                del request.session['cart']
                return redirect("home")
    else:
        # Si esta registrado pre rellenar
        if request.user.id:
            data = {'email': request.user.email, 'full_name': 'CXXX'}
        else:
            data= {}
        order_form = OrderForm(data)
        payment_form = MakePaymentForm()
        context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE }
        cart = request.session.get('cart', {})
        cart_items_and_total = get_cart_items_and_total(cart)
        context.update(cart_items_and_total)
    
    return render(request, "checkout/checkout.html", context)
