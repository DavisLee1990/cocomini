from django.test import TestCase

# Create your tests here.
temple="""
            <xml>
             <ToUserName>< ![CDATA[{}] ]></ToUserName> 
             <FromUserName>< ![CDATA[{}] ]></FromUserName> 
             <CreateTime>{}</CreateTime>
             <MsgType>< ![CDATA[text] ]></MsgType> 
             <Content>< ![CDATA[{}] ]></Content> 
            </xml>
            """
re=temple.format(1,2,3,4,5)

print(re)