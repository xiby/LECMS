from django.conf.urls import url
from . import views
from . import view_com
from django.contrib import admin

urlpatterns=[
    url(r'^admin/',admin.site.urls),
    # url(r'^login/',views.login,name="login"),
    url(r'^company/main/',view_com.main,name="main"),
    url(r'^company/login/',view_com.login,name="com_login"),
    url(r'company/showInv',view_com.searchInv,name="showInv"),
    url(r'company/givePrice',view_com.givePrice),
]