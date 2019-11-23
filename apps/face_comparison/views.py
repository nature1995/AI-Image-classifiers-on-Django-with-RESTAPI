from django.shortcuts import render
from django.http import HttpResponse
import requests
import AI.settings as config


# Create your views here.
def face_compare(request):
    return render(request, 'face-comparison.html')


def face_compare_request(request):
    api_key = config.API_KEY
    api_secret = config.API_SECRET
    response = requests.post('https://api-cn.faceplusplus.com/facepp/v3/compare', \
                             data={'api_key': api_key, 'api_secret': api_secret}, \
                             files=request.FILES)
    return HttpResponse(bytes.decode(response.content), content_type='application/json')