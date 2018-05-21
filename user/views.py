from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from user import models
import hashlib
import json
from django.db import IntegrityError

class Login(View):
    #基于CBV创建登录类
    def get(self,req):
        #处理登录页面
        return render(req,"user/login.html")

    def put(self,req):
        #用户修改密码
        pass

    def post(self,req):
        #用户登录
        res={
            "status":1,
            "error":None,
            "data":None
        }
        try:
            #处理提交页面
            user=req.POST.get("user")
            pwd=req.POST.get("pwd")
            md5_pwd=hashlib.md5(pwd.encode("utf8")).hexdigest()
            user=models.User.objects.filter(user_name=user,user_password=md5_pwd).first()
            if user:
                res["status"] = 1
                req.session['user_id'] = user.id  #用于user_id
                req.session['is_login'] = True  #用于登录验证
            else:
                res["status"]=0
                res["error"]="帐号/密码错误"
        except Exception as e:
                res["status"] = 0
                res["error"] = "请求错误"
        return HttpResponse(json.dumps(res))



class Registe(View):
    # 基于CBV创建注册用户类
    def get(self, req):
        # 处理登录页面
        return render(req, "user/registe.html")

    def post(self, req):
        #处理注册请求
        res = {
            "status": 1,
            "error": None,
            "data": None
        }
        #获取数据
        user = req.POST.get("user")
        pwd = req.POST.get("pwd")
        nick_name=req.POST.get("nick_name")
        email =req.POST.get("email")
        try:
            # 保存数据库
            models.User.objects.create(
                user_name=user,
                user_password=hashlib.md5(pwd.encode("utf8")).hexdigest(),
                user_nickname=nick_name,
                user_email=email
            )
            res["status"] = 1
        except IntegrityError as error:
            res["status"] = 0
            res["error"] = "用户已存在"
        return HttpResponse(json.dumps(res))

def user_info(req):
    return render(req,"user/info.html")

def login_util(func):
    '''
    登录验证装饰器
    :param func: 
    :return: 
    '''
    def wrapper(*args,**kwargs):
        try:
            if not args[0].session['is_login']:
                #如果没登录过，重定向到登录页面
                return redirect('/user/login/')
            else:
                data=func(*args,**kwargs)
                return data
        except Exception as e:
            return redirect('/user/login/')
    return wrapper