from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request,"template_app/first.html")


def weather(request):
    weather_dic={
        "istanbul":"30",
        "amsterdam":"40",
        "paris":[5,14,16,20],
        "rome":{"morning":10,"evening":20},
        "user_premium":True,
        "test":"testest"
            
    }
    
    return render(request,"template_app/weather.html",context=weather_dic)
