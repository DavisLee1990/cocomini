"""coco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from user import views

urlpatterns = [
    path('login/', views.Login.as_view()),  #get登录页面，put用户修改，post登录请求
    path('registe/',views.Registe.as_view()),   #get请求页面，post注册页面
    path('info/',views.user_info)  #用户个人信息页面
]
