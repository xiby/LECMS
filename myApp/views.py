from django.shortcuts import render
from django.http import HttpResponse

#以下是数据库内容
from myApp.models import UserInfo

# Create your views here.

def index(request):
    dataSet={'first':'3','second':'2'}
    if request.method=='POST':
        print(request.body)
    return render(request,"main.html",{'data':dataSet})

def login(request):
    if request.method=='POST':
        print(request.body)
        name=request.POST['username']
        pswd=request.POST['password']
        state=request.POST['state']
        print(name,pswd)
        # me=people()
        people=UserInfo.objects.all()
        print(people)
        try:
            one=UserInfo.objects.get(usr=name,pwd=pswd)
            print('登录成功')
        except:
            print('登录失败')
    return render(request,'login.html')