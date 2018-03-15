from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html' , context={
        'title': '我的页面',
        'welcome': '欢迎'
    })