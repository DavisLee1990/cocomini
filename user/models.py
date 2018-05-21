from django.db import models

# Create your models here.
class User(models.Model):
    #用户类
    user_name=models.CharField(u"用户名",max_length=45,unique=True,editable=False)
    user_password=models.CharField(u"密码",max_length=45,editable=False)
    user_nickname=models.CharField(u"昵称",max_length=4,unique=True)
    user_email=models.EmailField(u"Email")
    user_is_del=models.BooleanField(u"是否删除",default=False)
    user_create_time=models.DateTimeField(u"创建时间",editable=False,auto_now_add=True)
    user_update_time=models.DateTimeField(u"修改时间",editable=False,auto_now=True)
    user_del_time=models.DateTimeField(u"删除时间",editable=False,auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.user_name
    class Meta:
        db_table = 'Users'
        verbose_name_plural=u'用户'