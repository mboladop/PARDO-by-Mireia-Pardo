from django import forms
from .models import Order

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2015, 2036)]

    credit_card_number = forms.CharField(label='Numero de tarjeta', required=True,max_length=16)
    cvv = forms.CharField(label='Codigo de Seguridad (CVV)', required=True,max_length=3)
    expiry_month = forms.ChoiceField(label="Mes", choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(label="Año", choices=YEAR_CHOICES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
    
class OrderForm(forms.ModelForm):
    
    full_name = forms.CharField(label='Nombre Completo')
    phone_number = forms.CharField(label='Número de telefono')
    email = forms.EmailField(label='Email')
    country = forms.CharField(label='Pais')
    postcode = forms.CharField(label='Codigo postal')
    town_or_city = forms.CharField(label='Ciudad')
    street_address_1 = forms.CharField(label='Direccion 1')
    street_address_2 = forms.CharField(label='Direccion 2')
    county = forms.CharField(label='Comunidad')
    

    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'email', 'country', 'postcode', 'town_or_city', 'street_address_1', 'street_address_2', 'county')
        
        