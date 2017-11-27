from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def index(request):
    # 首页
    return render(request,'zixun/index.html')