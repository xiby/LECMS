#本文件用于处理公司视图，其所有操作以及页面跳转均在此文件中实现

import uuid
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from myApp.models import ComTable
from myApp.models import invTable
from myApp.models import bidTable

def login(request):
    '''模拟的公司登陆函数'''
    if request.method=='GET':
        return render(request,'comlogin_test.html')
    name=request.POST['username']
    pswd=request.POST['password']
    if request.method=='POST':
        try:
            print(name,pswd)
            company=ComTable.objects.get(ComID=name,ComPSW=pswd)
            response=redirect('/company/main/')
            response.set_cookie('comID',name)
            print(name,pswd)
            return response
        except:
            return render(request,'comlogin_test.html')

def main(request):
    '''公司登陆后看到的首个界面'''
    print(request.body)
    return render(request,'company.html')

def searchInv(request):
    if(request.method=='GET'):
        data=list()
        info=invTable.objects.filter(state=1)
        for item in info:
            tmp=dict()
            tmp['invNUM']=item.invNUM
            tmp['invCust']=item.invCust.CustID
            tmp['startPoint']=item.startPoint
            tmp['destination']=item.destination
            tmp['weight']=item.weight
            data.append(tmp)
        return render(request,'showInv.html',{'data':data})
    else:
        #此时公司提出竞标请求，应为其产生条竞标记录
        tmpbidNUM=uuid.uuid1()
        print(tmpbidNUM)
        tmpbidCom=request.COOKIES['comID']
        tmpinvNUM=request.POST['invNUM']
        tmpprice=request.POST['price']
        tmpdat=request.POST['dat']
        tmpinvNUM=request.POST['invNUM']
        try:
            tmpCom=ComTable.objects.get(ComID=tmpbidCom)
            tmpinv=invTable.objects.get(invNUM=tmpinvNUM)
            newbid=bidTable(bidNUM=tmpbidNUM,bidCom=tmpCom,price=tmpprice,costTime=tmpdat,mark=False,invNUM=tmpinv)
            newbid.save()
        except:
            pass
        print(request.POST)
        data=list()
        info=invTable.objects.filter(state=1)
        for item in info:
            tmp=dict()
            tmp['invNUM']=item.invNUM
            tmp['invCust']=item.invCust.CustID
            tmp['startPoint']=item.startPoint
            tmp['destination']=item.destination
            tmp['weight']=item.weight
            data.append(tmp)
        return render(request,'showInv.html',{'data':data})
        
def givePrice(request):
    if request.method=="GET":
        return render(request,'givePrice.html')
    else:
        pass
def orderManager(request):
    if request.method=='GET':
        return render(request,'')