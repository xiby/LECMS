#本文件用于处理公司视图，其所有操作以及页面跳转均在此文件中实现

from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    '''公司登陆后看到的首个界面'''
    return render(request,'company.html')