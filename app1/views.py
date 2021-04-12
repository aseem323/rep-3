from django.shortcuts import render
from django.http import HttpResponse 

def test(request):
    return HttpResponse('hii')
def test1(request):
    return HttpResponse('heloooo')
def test2(request):
    return render(request,'new.html')
def test3(request):
    return render(request,'loginform.html')

# Create your views here.
