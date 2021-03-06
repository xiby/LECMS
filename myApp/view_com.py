#本文件用于处理公司视图，其所有操作以及页面跳转均在此文件中实现

import uuid
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from myApp.models import CustTable
from myApp.models import ComTable
from myApp.models import invTable
from myApp.models import bidTable
from myApp.models import price
from myApp.models import orderTable

import datetime


state=['待发货','运输中','已送达','确认送达','交易成功']
def login(request):
    '''模拟的公司登陆函数'''
    if request.method=='GET':
        return render(request,'comlogin_test.html')
    if request.method=='POST':
        name=request.POST['username']
        pswd=request.POST['password']
        try:
            # print(name,pswd)
            company=ComTable.objects.get(ComID=name,ComPSW=pswd)
            response=redirect('/myApp/company/main/')
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
        comp=request.COOKIES['comID']
        tmpWeight=request.POST['weight']
        tmpPrice=request.POST['price']
        print(tmpWeight,tmpPrice)
        company=ComTable.objects.get(ComID=comp)
        cp=price(ComNUM=company,weight=tmpWeight,pricing=tmpPrice)
        cp.save()
        print('保存成功')
        return render(request,'givePrice.html')
def orderManager(request):
    if request.method=='POST' and request.POST['pname']=='logi':
        # print()
        ordernum=request.POST['ordernum']
        next=request.POST['nextposition']
        try:
            order=orderTable.objects.get(orderNUM=ordernum,state__lt=2)
            order.loginfo=order.loginfo+' '+next
            if int(next)==order.destination:
                order.state=2
            order.save()
        except:
            pass
    if request.method=='POST' and request.POST['pname']=='deliver':
        ordernum=request.POST['ordernum']
        try:
            order=orderTable.objects.get(orderNUM=ordernum,state=0)
            order.state=1
            order.loginfo=order.startPoint
            order.startDate=datetime.datetime.now().strftime('%Y-%m-%d')
            order.save()
        except:
            pass
    comID=request.COOKIES['comID']
    data1=list()
    data2=list()
    try:
        company=ComTable.objects.get(ComID=comID)
        ans=orderTable.objects.filter(ComID=company,state__lt=3,state__gt=0)
        for item in ans:
            d=dict()
            d['orderNUM']=item.orderNUM
            d['startPoint']=item.startPoint
            d['destination']=item.destination
            d['position']=item.loginfo.split(' ')[-1]
            d['optmpath']=item.optmpath
            d['custID']=item.CustID.CustID
            d['startDate']=item.startDate
            d['state']=state[item.state]
            data1.append(d)
    except:
        pass
    try:
        company=ComTable.objects.get(ComID=comID)
        ans=orderTable.objects.filter(ComID=company,state=0)
        for item in ans:
            d=dict()
            d['orderNUM']=item.orderNUM
            d['CustID']=item.CustID.CustID
            d['startPoint']=item.startPoint
            d['destination']=item.destination
            d['state']=state[item.state]
            data2.append(d)
    except:
        pass
    return render(request,'orderManger.html',{"data":{"data1":data1,"data2":data2}})