# coding=UTF-8
from django.urls import path
from . import views
# 修改後
urlpatterns = [
    # 後方的 name 可以先忽略，目前不會用到
    # 這邊的網址不需再加 vendor,在HelloWorld的urls.py已經用includ 了
    path('', views.showtemplate, name="vendor_index"),
]