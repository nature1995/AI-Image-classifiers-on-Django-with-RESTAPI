from django.shortcuts import render
from django.http import HttpResponse
import requests
import AI.settings as config
import hashlib
import time
import random
import string
from urllib.parse import quote
import requests


def tenc_ai(request):
    get_sentiments(request)
    get_content(request)
    return render(request, 'tenc_ai.html')


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    return m.hexdigest().upper()


def get_params2(plus_item):
    global params
    t = time.time()
    time_stamp=str(int(t))
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    app_id='2111918951'
    app_key='oGryHSSYbDTnvCSJ'
    params = {'app_id': app_id,
              'text': plus_item,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
             }
    sign_before = ''
    for key in sorted(params):
        sign_before += '{}={}&'.format(key,quote(params[key], safe=''))
    sign_before += 'app_key={}'.format(app_key)
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params


def get_params1(plus_item):
    global params
    t = time.time()
    time_stamp = str(int(t))
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    app_id = '2111918951'
    app_key = 'oGryHSSYbDTnvCSJ'
    params = {'app_id': app_id,
              'question': plus_item,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              'session': '10000'
              }
    sign_before = ''
    for key in sorted(params):
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    sign_before += 'app_key={}'.format(app_key)
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params


def get_content(plus_item):
    global payload, r
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    plus_item = plus_item.POST.get('text1', None)
    plus_item = plus_item.encode('utf-8')
    payload = get_params1(plus_item)
    # r = requests.get(url,params=payload)  
    r = requests.post(url, data=payload)
    print(r.json()["data"]["answer"])


def get_sentiments(request):
    if request.POST:
         print('Having submit')
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"
    comments = request.POST.get('text', None)
    comments = comments.encode('utf-8')
    payload = get_params2(comments)
    r = requests.post(url,data=payload)
    print(r.json())
    # return render(request, 'tenc_ai.html')

