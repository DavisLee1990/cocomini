from django.shortcuts import render
# Create your views here.
from django.shortcuts import HttpResponse,redirect
import hashlib
from cocomini.settings import wechat_config
import json
from django.views import View
# from wechat.wechat_controller import MsgDispatcher
from django.views.decorators.csrf import csrf_exempt
import time
from wechat.wechat_util import WechatUtil
from wechat.wechat_controller import Handler

TOKEN=wechat_config["token"]


@csrf_exempt
def weixin_main(req):
    if req.method == "GET":
        '''
        验证微信服务器的GET方法
        :param req: 
        :return: 返回微信服务器随机字符串
        '''
        # this's verify server is valid for wechat(这是微信验证服务器是否存在)
        signature = req.GET.get("signature")  # 加密签名
        timestamp = req.GET.get("timestamp")  # 时间戳
        nonce = req.GET.get("nonce")  # 随机数
        echostr = req.GET.get("echostr")  # 随机字符串
        if signature and timestamp and nonce and echostr:
            # 根据文档对token,timestamp,nonce字典序排序成字符串后进行sha1加密
            verify_data = [TOKEN, timestamp, nonce]
            verify_data.sort()
            str = ''.join(verify_data)
            s = hashlib.sha1(str.encode()).hexdigest()
            if s == signature:
                # 通过则是微信服务器的请求\
                return HttpResponse(echostr)
    else:
        data=WechatUtil().getData(req)  #从微信工具类获取数据
        handle=Handler()
        if hasattr(handle,data["msgType"]):
            handle=getattr(handle,data["msgType"])
            result=handle(data)
            return HttpResponse(result)
        else:
            pass
        # result=wechat_controller(data) #
        # print("返回的结果为:",result)














        # webData = req.body
        # xmlData = ET.fromstring(webData)
        # msg_type = xmlData.find('MsgType').text
        # ToUserName = xmlData.find('ToUserName').text
        # FromUserName = xmlData.find('FromUserName').text
        # CreateTime = xmlData.find('CreateTime').text
        # MsgType = xmlData.find('MsgType').text
        # MsgId = xmlData.find('MsgId').text
        # toUser = FromUserName
        # fromUser = ToUserName
        # if msg_type == 'text':
        #     content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
        #     replyMsg = TextMsg(toUser, fromUser, content)
        # elif msg_type == 'image':
        #     content = "图片已收到,谢谢"
        #     replyMsg = TextMsg(toUser, fromUser, content)
        # elif msg_type == 'voice':
        #     content = "语音已收到,谢谢"
        #     replyMsg = TextMsg(toUser, fromUser, content)
        # elif msg_type == 'video':
        #     content = "视频已收到,谢谢"
        #     replyMsg = TextMsg(toUser, fromUser, content)
        # elif msg_type == 'shortvideo':
        #     content = "小视频已收到,谢谢"
        #     replyMsg = TextMsg(toUser, fromUser, content)
        # elif msg_type == 'location':
        #     content = "位置已收到,谢谢"
        #     replyMsg = TextMsg(toUser, fromUser, content)
        # else:
        #     msg_type == 'link'
        #     content = "链接已收到,谢谢"
        #     replyMsg = TextMsg(toUser, fromUser, content)
        # res=replyMsg.send()
        # return HttpResponse(res)