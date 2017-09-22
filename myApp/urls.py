from django.conf.urls import url
from . import views
from . import view_com
from django.contrib import admin

urlpatterns=[
    url(r'^admin/',admin.site.urls),
    url(r'^login/',views.login,name="login"),
    url(r'^company/main/',view_com.main,name="main")
]