from django.shortcuts import render,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt


def test(request):
    return render(request,'detect_object.html')


@csrf_exempt
def ajax(request):
    if request.method=="POST":
        name=request.POST.get('name')
        print("ok")
        status=1
        result="sucuss"
        return HttpResponse(json.dumps({
            "status":status,
            "result":result,
            "name":name
        }))