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
from novel import views

urlpatterns = [
    path('index/', views.index),  # 登录后主页面请求处理
    path('bookrack/', views.Bookrack.as_view()),  # get 查,post 增,delete 删
    path("bookstore/", views.bookstore),  # 处理书城请求
    path("<int:novel_id>", views.novelDetail),  # 处理图书详情请求
    path("catalog/<int:novel_type>-<int:novel_id>", views.catalog_page),  # 书籍目录页面请求
    path("catalog/<int:novel_type>-<int:novel_id>-<int:page_num>", views.catalog_data),  # 书籍目录数据加载
    path("chapter/content/<int:novel_type>-<int:novel_id>-<int:chapter_id>", views.chapterContent), #书籍内容页面请求
    path("booksearch/", views.booksearch),#处理图书搜索请求
    path("test/", views.test)
]
