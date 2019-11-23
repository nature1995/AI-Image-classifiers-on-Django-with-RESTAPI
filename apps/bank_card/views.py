from django.shortcuts import render
from django.http import HttpResponse
import requests
import AI.settings as config


# Create your views here.
def bank_card(request):
    return render(request, 'bank-card.html')


def bank_card_request(request):
    api_key = config.API_KEY
    api_secret = config.API_SECRET
    response = requests.post('https://api-cn.faceplusplus.com/cardpp/v1/ocrbankcard', \
                             data={'api_key': api_key, 'api_secret': api_secret}, \
                             files=request.FILES)
    return HttpResponse(bytes.decode(response.content), content_type='application/json')
