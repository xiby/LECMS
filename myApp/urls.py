from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns=[
    url(r'^admin/',admin.site.urls),
    url(r'^login/',views.login,name="login"),
]