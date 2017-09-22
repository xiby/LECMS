#本文件用于处理公司视图，其所有操作以及页面跳转均在此文件中实现

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from myApp.models import ComTable

def login(request):
    '''模拟的公司登陆函数'''
    if request.method=='GET':
        return render(request,'comlogin_test.html')
    name=request.POST['username']
    pswd=request.POST['password']
    if request.method=='POST':
        try:
            company=ComTable.objects.get(ComID=name,ComPSW=pswd)
            return HttpResponseRedirect('/myApp/company/main')
        except:
            return render(request,'comlogin_test.html')

def main(request):
    '''公司登陆后看到的首个界面'''
    return render(request,'company.html')