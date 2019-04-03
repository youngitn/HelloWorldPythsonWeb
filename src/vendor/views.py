# coding=UTF-8
from django.shortcuts import render
from .models import Vendor,Food
# Create your views here.


# Create your views here.
# def showtemplate(request):
#     # 今天先不探討什麼是 render，先記得它會去撈 test.html
#     return render(request, 'test.html')

def showtemplate(request):
    vendor_list = Vendor.objects.all() # 把所有 Vendor 的資料取出來
    f_list = Food.objects.all()
    context = {'vendor_list': vendor_list,'food_list':f_list} # 建立 Dict對應到Vendor的資料，
    return render(request, 'test.html', context)