from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("第一个页面")
def index2(request):
    return HttpResponse("第二个页面")