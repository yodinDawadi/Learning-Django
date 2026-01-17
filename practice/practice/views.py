from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    #return HttpResponse("This is home page")
    
    return render(request,'index.html')

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")
