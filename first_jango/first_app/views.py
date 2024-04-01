from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

courses_dic={
    "python": "python course page",
    "java":"java courses page",
    "kotlin":"kotlin courses page",
    "swift":"swift courses page"
        
}
def mert(requests,num1):
    if num1==10:
        return HttpResponseRedirect("https://www.youtube.com/watch?v=C2mRvE6UvWM")
    else:
        return HttpResponseNotFound("not found! please look another courses")
        

def index(request):
    return HttpResponse("this is afirst janga projecct")



def courses(request,item):
    try:
        course=courses_dic[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("not found! please look another courses")
        #raise Http404()
        #return HttpResponse(courses_dic.get(item,"not found"))




def carpma(request,num1,num2):
    return HttpResponse(f"{num1}* {num2}={num1 * num2}")
""""
def coursenumber(request,num1):
    courrse_list=list(courses_dic.keys())
    try:
        course=courrse_list[num1]
        
        return HttpResponseRedirect(reverse("course",args=[course]))
    except:
        return HttpResponseNotFound("not found! please look another courses")
    
"""
    
    
    
  

