from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Url_model
import random
import string
# Create your views here.

@api_view(['POST'])
def create_code_view(requests,*args, **kwargs):
    url_model = Url_model()
    url = requests.data["url"]
    letters_and_digits = string.ascii_lowercase + string.digits

    code = ''.join((random.choice(letters_and_digits) for i in range(5)))
    
    while Url_model.objects.filter(code=code).exists():
            code = ''.join((random.choice(letters_and_digits) for i in range(5)))
        
    url_model.url = url.strip()
    url_model.code = code
    url_model.save()
    return Response(data={"url":url_model.url,"code":url_model.code},status=200)


@api_view(['GET'])
def find_code_view(requests,code,*args, **kwargs):
    qs = Url_model.objects.filter(code=code)
    if not qs.exists():
        return redirect("/")
    try:
        return redirect(qs.first().url)

    except :
        return render(requests,'home.html',context={"error":"invalid_url"})
        

@api_view(['GET'])
def home_view(requests,*args, **kwargs):
    return render(requests,'home.html')
    
    
