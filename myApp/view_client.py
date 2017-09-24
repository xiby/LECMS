import uuid
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from myApp.models import CustTable
from myApp.models import invTable
from myApp.models import bidTable
from myApp.models import price

def show(request):
    if request.method=='GET':
        return render(request,'Welcome.html')
    return render(request,'Welcome.html')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST' and request.POST['type']=="signin":
        custID=request.POST['username']
        psw=request.POST['password']
        print(custID,psw)
        try:
            man=CustTable.objects.get(CustID=custID,CustPSW=psw)
            response=redirect('/myApp/client/main')
            response.set_cookie('custID',custID)
            return response
        except:
            pass
    return render(request,'login.html')

def main(request):
    if request.method=='GET':
        return render(request,'client1.html')

def showPrice(request):
    if request.method=='GET':
        priceinfo=price.objects.all()
        data=list()
        for item in priceinfo:
            d=dict()
            d['ComNUM']=item.ComNUM.ComID
            d['weight']=item.weight
            d['pricing']=item.pricing
            data.append(d)
        return render(request,'showPrice.html',{'data':data})

def giveInv(request):
    if request.method=='GET':
        return render(request,'giveInv.html')
    if request.method=='POST':
        '''此时应该生成一个招标记录'''
        num=uuid.uuid1()
        cust=CustTable.objects.get(CustID=request.COOKIES['custID'])
        print('找寻用户成功')
        sPoint=request.POST['startPoint']
        dest=request.POST['destination']
        tmpweight=request.POST['weight']
        newInv=invTable(invNUM=num,invCust=cust,startPoint=sPoint,destination=dest,weight=tmpweight,state=True)
        newInv.save()
        print('保存成功')
        return render(request,'giveInv.html')
def showBid(request):
    if request.method=='GET':
        data=list()
        cust=request.COOKIES['custID']
        man=CustTable.objects.get(CustID=cust)
        query_ans=invTable.objects.filter(invCust=man,state=True)
        for item in query_ans:
            query_ans2=bidTable.objects.filter(invNUM=item)
            for tmp in query_ans2:
                d=dict()
                d['invNUM']=item.invNUM
                d['bidNUM']=tmp.bidNUM
                d['startPoint']=item.startPoint
                d['destination']=item.destination
                d['weight']=item.weight
                d['comNUM']=tmp.bidCom.ComID
                d['price']=tmp.price
                d['priod']=tmp.costTime
                data.append(d)
        return render(request,'showbid.html',{"data":data})