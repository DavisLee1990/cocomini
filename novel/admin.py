from django.contrib import admin

# Register your models here.
from novel import models
class NovelAdmin(admin.ModelAdmin):
    list_display = ("novel_title","novel_author","novel_status","novel_type","novel_intro")

class UserNovelAdmin(admin.ModelAdmin):
    list_display = ("user","novel","grade")



class QihuanChaptersAdmin(admin.ModelAdmin):
    list_display = ("novel","chapter_title","chapter_content")

class WuxiaChaptersAdmin(admin.ModelAdmin):
    list_display = ("novel", "chapter_title", "chapter_content")

class DoushiChaptersAdmin(admin.ModelAdmin):
    list_display = ("novel", "chapter_title", "chapter_content")

class LishiChaptersAdmin(admin.ModelAdmin):
    list_display = ("novel", "chapter_title", "chapter_content")

class KehuanChaptersAdmin(admin.ModelAdmin):
    list_display = ("novel", "chapter_title", "chapter_content")

class WangyouChaptersAdmin(admin.ModelAdmin):
    list_display = ("novel", "chapter_title", "chapter_content")

class NvshengChaptersAdmin(admin.ModelAdmin):
    list_display = ("novel", "chapter_title", "chapter_content")

admin.site.register(models.Novel,NovelAdmin)
admin.site.register(models.User_Novel,UserNovelAdmin)
admin.site.register(models.Qihuan_chapters,QihuanChaptersAdmin)
admin.site.register(models.Wuxia_chapters,WuxiaChaptersAdmin)
admin.site.register(models.Doushi_chapters,DoushiChaptersAdmin)
admin.site.register(models.Lishi_chapters,LishiChaptersAdmin)
admin.site.register(models.Kehuan_chapters,KehuanChaptersAdmin)
admin.site.register(models.Wangyou_chapters,WangyouChaptersAdmin)
admin.site.register(models.Nvsheng_chapters,NvshengChaptersAdmin)