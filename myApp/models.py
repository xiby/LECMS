from django.db import models

# Create your models here.

class UserInfo(models.Model):           #测试用表
    usr=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)

class CustTable(models.Model):          #用户信息表
    CustID=models.CharField(max_length=10)      #用户注册时，以及之后用于登陆的用户名
    CustPSW=models.CharField(max_length=15)     #用户用于登陆的密码

class ComTable(models.Model):           #公司信息表
    ComID=models.CharField(max_length=10)       #公司注册时，以及之后用于登陆的用户名
    ComPSW=models.CharField(max_length=15)      #公司用于登陆的密码
    ComName=models.CharField(max_length=20)     #公司名称
    ComArea=models.CharField(max_length=100)                  #公司覆盖范围，用字符串来表示，不同的地点之间用空格来分隔开，便于处理

class invTable(models.Model):           
    '''招标表，由用户创建，一位用户可以发布很多招标信息，
    但一份招标信息只能由一位用户来创建，
    可被所有公司看到'''
    invNUM=models.CharField(max_length=20,primary_key=True)     #每一份招标记录的唯一编号
    invCust=models.ForeignKey(CustTable,on_delete=models.CASCADE)   #发布招标信息的用户
    startPoint=models.IntegerField()            #用户要求的起点城市，用编号来实现
    destination=models.IntegerField()           #用户要求的终点城市，也用编号来实现
    weight=models.FloatField()                  #！！！！！！！！！！！新增的属性用户货物的重量
    state=models.BooleanField()                 #当前招标记录的状态

class bidTable(models.Model):           #投标表，由公司创建
    bidNUM=models.CharField(max_length=20,primary_key=True)             #每一份投标记录的唯一编号
    bidCom=models.ForeignKey(ComTable,on_delete=models.CASCADE,default=None)
    invNUM=models.ForeignKey(invTable,on_delete=models.Ct="123")      
    #投标公司的ID，设置为级联删除，且默认设置为空，等交易确认后再填写对应字段
    price=models.IntegerField()         #投标公司发布的价格
    costTime=models.FloatField()        #！！！！！！！！！！此处将原来的时间换成了最长所用时间
    mark=models.BooleanField()          #标注该投标信息是否被处理的标志位

class orderTable(models.Model):
    '''订单表，在竞标结束后自动创建'''
    orderNUM=models.CharField(max_length=20,primary_key=True)       #每一份订单对应的唯一编号
    startPoint=models.IntegerField()        #订单的起始城市
    destination=models.IntegerField()       #订单的终点
    CustID=models.ForeignKey(CustTASCADE,defaulable,on_delete=models.CASCADE)       #产生订单的用户，参考用户表
    ComID=models.ForeignKey(ComTable,on_delete=models.CASCADE)         #产生订单的公司，参考公司表
    cost=models.IntegerField()          #订单的费用，由公司给出
    startDate=models.DateField()        #！！！！！！新增------订单的产生日期
    costTime=models.IntegerField()      #运输实际花费的时间，在完成后填写
    state=models.CharField(max_length=10)   #订单的状态，包括待发货等等
    loginfo=models.CharField(max_length=100)    #物流信息，用字符串来表示，不同城市用空格按顺序隔开

class carTable(models.Model):
    '''车辆信息表，为公司所有'''
    carNUM=models.CharField(primary_key=True,max_length=15)     #车牌号，主码
    comID=models.ForeignKey(ComTable,on_delete=models.CASCADE) #车辆所属公司，参考公司表
    avaiable=models.BooleanField()      #车辆的可用状态
    city=models.IntegerField()          #车辆所属城市
    load=models.FloatField()            #车辆的最大负重

class feedback(models.Model):
    '''用户反馈表：
        在订单结束后，用户填写此记录
        为用户提供反馈通道，公司能够看到并回复
    '''
    orderNUM=models.ForeignKey(orderTable,on_delete=models.CASCADE,primary_key=True)    #反馈对应的订单号
    info=models.CharField(max_length=100)       #用户的反馈信息
    replyinfo=models.CharField(max_length=100)         #回复信息
    state=models.BooleanField()             #处理信息

class price(models.Model):
    '''公司给出的报价表，由公司来填写并修改，用户只能查询'''
    ComNUM=models.ForeignKey(ComTable,on_delete=models.CASCADE)     #给出报价的公司
    weight=models.IntegerField()        #货物重量
    price=models.IntegerField()         #价格/元
