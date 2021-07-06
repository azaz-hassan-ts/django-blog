from django.http import HttpResponse
from django.shortcuts import render

#write your views here

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'home/homepage.html',)

def about(request):
    # return HttpResponse('homepage')
    return render(request, 'home/about.html',)


