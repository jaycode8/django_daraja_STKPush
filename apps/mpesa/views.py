from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

# Create your views here.

def index(req):
    cl = MpesaClient()
    phone_number = '0111482180'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://safariadventure.vercel.app/'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(req):
    data = req.body
    print(data)
    return HttpResponse("STK Push in Django")
