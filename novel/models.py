from django.db import models

# Create your models here.
class Novel(models.Model):
    #小说类
    novel_id=models.AutoField(primary_key=True)
    novel_title = models.CharField(u"图书名字",max_length=90)
    novel_img =models.CharField(u"封面地址",max_length=100)
    novel_author=models.CharField(u"图书作者",max_length=45,null=True,blank=True)
    status_type=(
        (0,u"连载中"),
        (1,u"完结")
    )
    novel_status=models.SmallIntegerField(u"图书状态",choices=status_type,default=0)
    type=(
        (0,u"奇幻/玄幻"),
        (1,u"武侠/仙侠"),
        (2,u"都市/言情"),
        (3,u"历史/军事"),
        (4,u"科幻/灵异"),
        (5,u"网游/竞技"),
        (6,u"女生频道")
    )
    novel_type = models.IntegerField(u"图书类型",choices=type,default=1)
    novel_intro = models.TextField(u"图书简介",null=True,blank=True)
    def __str__(self):
        return self.novel_title

    class Meta:
        db_table = 'novels'
        verbose_name_plural = u'图书'


class User_Novel(models.Model):
    #用户-小说的多对多关系建立的中间表
    user=models.ForeignKey("user.User",to_field="id",on_delete=models.CASCADE,verbose_name="用户")#用户id
    novel=models.ForeignKey("novel.Novel",to_field="novel_id",on_delete=models.CASCADE,verbose_name="图书")#小说id
    grade=models.IntegerField(u"图书评分",null=True,blank=True)
    class Meta:
        db_table = 'Users_Novels'
        verbose_name_plural = u'用户/图书'

    def __str__(self):
        return "'%s'的图书：'%s'"%(self.user.user_name,self.novel.novel_title)

#以下为章节models
# class Chapter:
#     chapter_id = models.AutoField(primary_key=True)
#     novel_id=models.ForeignKey("novel.Novel",to_field="novel_id",on_delete=models.CASCADE)#关联小说id
#     chapter_title=models.CharField(max_length=90)#章节的名字
#     chapter_content=models.TextField()#章节内的内容

#由于数据量过大,对章节内容进行分表
class Qihuan_chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    novel = models.ForeignKey("novel.Novel", to_field="novel_id", on_delete=models.CASCADE)  # 关联小说id
    chapter_title = models.CharField(max_length=90)  # 章节的名字
    chapter_content = models.TextField()  # 章节内的内容
    def __str__(self):
        return self.chapter_title

    class Meta:
        db_table = 'Qihuan_chapters'
        verbose_name_plural = u'(奇幻/玄幻)章节'
class Wuxia_chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    novel = models.ForeignKey("novel.Novel", to_field="novel_id", on_delete=models.CASCADE)  # 关联小说id
    chapter_title = models.CharField(max_length=90)  # 章节的名字
    chapter_content = models.TextField()  # 章节内的内容
    def __str__(self):
        return self.chapter_title

    class Meta:
        db_table = 'Wuxia_chapters'
        verbose_name_plural = u'(武侠/仙侠)章节'
class Doushi_chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    novel = models.ForeignKey("novel.Novel", to_field="novel_id", on_delete=models.CASCADE)  # 关联小说id
    chapter_title = models.CharField(max_length=90)  # 章节的名字
    chapter_content = models.TextField()  # 章节内的内容
    def __str__(self):
        return self.chapter_title

    class Meta:
        db_table = 'Doushi_chapters'
        verbose_name_plural = u'(都市/言情)章节'
class Lishi_chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    novel = models.ForeignKey("novel.Novel", to_field="novel_id", on_delete=models.CASCADE)  # 关联小说id
    chapter_title = models.CharField(max_length=90)  # 章节的名字
    chapter_content = models.TextField()  # 章节内的内容
    def __str__(self):
        return self.chapter_title

    class Meta:
        db_table = 'Lishi_chapters'
        verbose_name_plural = u'(历史/军事)章节'
class Kehuan_chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    novel = models.ForeignKey("novel.Novel", to_field="novel_id", on_delete=models.CASCADE)  # 关联小说id
    chapter_title = models.CharField(max_length=90)  # 章节的名字
    chapter_content = models.TextField()  # 章节内的内容
    def __str__(self):
        return self.chapter_title

    class Meta:
        db_table = 'Kehuan_chapters'
        verbose_name_plural = u'(科幻/灵异)章节'
class Wangyou_chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    novel = models.ForeignKey("novel.Novel", to_field="novel_id", on_delete=models.CASCADE)  # 关联小说id
    chapter_title = models.CharField(max_length=90)  # 章节的名字
    chapter_content = models.TextField()  # 章节内的内容
    def __str__(self):
        return self.chapter_title

    class Meta:
        db_table = 'Wangyou_chapters'
        verbose_name_plural = u'(网游/竞技)章节'
class Nvsheng_chapters(models.Model):
    chapter_id = models.AutoField(primary_key=True)
    novel = models.ForeignKey("novel.Novel", to_field="novel_id", on_delete=models.CASCADE)  # 关联小说id
    chapter_title = models.CharField(max_length=90)  # 章节的名字
    chapter_content = models.TextField()  # 章节内的内容
    def __str__(self):
        return self.chapter_title

    class Meta:
        db_table = 'Nvsheng_chapters'
        verbose_name_plural = u'(女生频道)章节'
