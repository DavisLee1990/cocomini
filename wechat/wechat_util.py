# -*- coding:utf-8 -*-
#Author:Davis
import xml.etree.ElementTree as ET

class WechatUtil:
    '''
    微信工具类
    '''

    def getData(self,req):
        '''
        获取微信发送过来的消息
        :return: 提取后的消息字典
        '''
        data={}

        webData = req.body
        xmlData = ET.fromstring(webData)
        data["msgType"] = xmlData.find('MsgType').text #消息类型，固定存在
        data["toUserName"] = xmlData.find('ToUserName').text #发送给公众号用户
        data["fromUserName"] = xmlData.find('FromUserName').text #发送的公众号
        data["createTime"] = xmlData.find('CreateTime').text #微信服务器访问的时间
        #文本消息
        if data["msgType"] == "text":
            data["content"] = xmlData.find("Content").text if xmlData.find("Content") is not None else ""
            data["msgId"] = xmlData.find("msgId").text if xmlData.find("msgId") is not None else ""
        #图片消息
        if data["msgType"] == "image":
            data["picUrl"] = xmlData.find("PicUrl").text if xmlData.find("PicUrl") is not None else ""
            data["mediaId"] = xmlData.find("MediaId").text if xmlData.find("MediaId") is not None else ""
            data["msgId"] = xmlData.find("msgId").text if xmlData.find("msgId") is not None else ""
        #语音消息
        if data["msgType"] == "voice":
            data["mediaId"] = xmlData.find("MediaId").text if xmlData.find("MediaId") is not None else ""
            data["format"] = xmlData.find("Format").text if xmlData.find("Format") is not None else ""
            data["recognition"] = xmlData.find("Recognition").text if xmlData.find("Recognition") is not None else ""
            data["msgId"] = xmlData.find("msgId").text if xmlData.find("msgId") is not None else ""
        #视频消息
        if data["msgType"] == "video":
            data["mediaId"] = xmlData.find("MediaId").text if xmlData.find("MediaId") is not None else ""
            data["thumbMediaId"] = xmlData.find("ThumbMediaId").text if xmlData.find("ThumbMediaId") is not None else ""
            data["msgId"] = xmlData.find("msgId").text if xmlData.find("msgId") is not None else ""
        #小视频消息
        if data["msgType"] == "shortvideo":
            data["mediaId"] = xmlData.find("MediaId").text if xmlData.find("MediaId") is not None else ""
            data["format"] = xmlData.find("Format").text if xmlData.find("Format") is not None else ""
            data["msgId"] = xmlData.find("msgId").text if xmlData.find("msgId") is not None else ""
        #地理位置消息
        if data["msgType"] == "location":
            data["location_X"] = xmlData.find("Location_X").text if xmlData.find("Location_X") is not None else ""
            data["location_Y"] = xmlData.find("Location_Y").text if xmlData.find("Location_Y") is not None else ""
            data["scale"] = xmlData.find("Scale").text if xmlData.find("Scale") is not None else ""
            data["label"] = xmlData.find("Label").text if xmlData.find("Label") is not None else ""
        #链接消息
        if data["msgType"] == "link":
            data["title"] = xmlData.find("Title").text if xmlData.find("Title") is not None else ""
            data["description"] = xmlData.find("Description").text if xmlData.find("Description") is not None else ""
            data["url"] = xmlData.find("Url").text if xmlData.find("Url") is not None else ""
            data["msgId"] = xmlData.find("msgId").text if xmlData.find("msgId") is not None else ""
        #事件消息
        if data["msgType"] == "event":
            data["event"] = xmlData.find("Event").text if xmlData.find("Event") is not None else ""

        return data


    def sendTextMsg(self,toUserName,fromUserName,time,content):
        '''
        发送普通文本消息
        :param content: 
        :return: 
        '''
        XmlForm = """
            <xml>
            <ToUserName><![CDATA[{}]]></ToUserName>
            <FromUserName><![CDATA[{}]]></FromUserName>
            <CreateTime>{}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{}]]></Content>
            </xml>
        """
        return XmlForm.format(toUserName,fromUserName,time,content)

    def sendPicTextMsg(self,toUserName,fromUserName,time,data):
        '''
        图文消息
        :param toUserName: 
        :param fromUserName: 
        :param time: 
        :param data: 图文对象
        :return: 
        '''
        XmlForm="""
        <xml>
            <ToUserName>< ![CDATA[{}] ]></ToUserName>
            <FromUserName>< ![CDATA[{}] ]></FromUserName>
            <CreateTime>{}</CreateTime>
            <MsgType>< ![CDATA[news] ]></MsgType>
            <ArticleCount>{}</ArticleCount>
            <Articles>
        """
        baseXml=XmlForm.format(toUserName, fromUserName, time,len(data))
        for i in range(len(data)):
            baseXml+="""<item>
                            <Title>< ![CDATA["""+data[i]["title"]+"""] ]></Title>
                            <Description>< ![CDATA["""+data[i]["description"]+"""] ]></Description>
                            <PicUrl>< ![CDATA["""+data[i]["picUrl"]+"""] ]></PicUrl>
                            <Url>< ![CDATA["""+data[i]["url"]+"""] ]></Url>
                        </item>
                    """
        baseXml+="</Articles></xml>"
        return baseXml








