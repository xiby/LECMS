from django.conf.urls import url
from . import views
from . import view_com
from . import view_client
from django.contrib import admin

urlpatterns=[
    url(r'^admin/',admin.site.urls),
    # url(r'^login/',views.login,name="login"),
    url(r'client/login',view_client.login,name='client_login'),
    url(r'client/show',view_client.show,name="client_main"),
    url(r'client/main',view_client.main,name="client_show"),
    url(r'client/ShowPrice',view_client.showPrice),
    url(r'client/ShowBid',view_client.showBid),
    url(r'client/giveInv',view_client.giveInv),
    url(r'^company/main/',view_com.main,name="main"),
    url(r'^company/login/',view_com.login,name="com_login"),
    url(r'company/showInv',view_com.searchInv,name="showInv"),
    url(r'company/givePrice',view_com.givePrice),
    url(r'company/orderManger',view_com.orderManager),
]