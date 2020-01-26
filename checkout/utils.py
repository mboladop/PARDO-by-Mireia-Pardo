from django.shortcuts import get_object_or_404
from products.models import Product
from .forms import OrderForm
import requests 
from .models import *
import stripe
from cart import *
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET

def save_order_items(order, cart):
    for item in cart:
        product = get_object_or_404(Product, pk=item['product'])
        # define size
        order_line_item = OrderLineItem(
            order = order,
            product = product,
            # size = item['size'],
            quantity = item['total']
            )
        order_line_item.save()
        
def charge_card(stripe_token, total):
    total_in_cent = int(total*100)
    return stripe.Charge.create(
        amount=total_in_cent,
        currency="EUR",
        description="Dummy Transaction",
        card=stripe_token,
    )

def send_confirmation_email(email, username, items_and_total):
    context = {
        'site_name': "pardobymireiapardo.com",
        'user': username,
    }
    context.update(items_and_total)
    message = render_to_string('checkout/text_confirmation_email.html', context)
    html_message = render_to_string('checkout/html_confirmation_email.html', context)
                
    subject = '¡Gracias por tu compra!'
    message = message
    from_email = settings.SYSTEM_EMAIL
    to_email = [email]
    
        
    
    # send_mail(subject,message,from_email,to_email,fail_silently=False,html_message=html_message)
    requests.post("https://api.mailgun.net/v3/sandboxc9e94be3f59843eabeb382f76eb9faf7.mailgun.org/messages",auth=("api", "5ac1621fbea4f2ff722c0a2068a3334d-16ffd509-88d58809"), 
    data={"from": "Pardo by Mireia Pardo <pardobymireia@gmail.com>","to": to_email,"subject": subject,"text": message})
    
    
    