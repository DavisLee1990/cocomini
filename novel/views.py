from django.shortcuts import render, HttpResponse
from django.views import View
from novel import models
import json
from cocomini.settings import page_config
from user.views import login_require
from django.http import QueryDict
@login_require
def index(req):
    return render(req, "novel/index.html")

class Bookrack(View):
    def get(self,req):
        user_id = req.session.get("user_id")
        novels = models.User_Novel.objects.filter(user_id=user_id).all()
        return render(req, "novel/book_rack.html", {'novels': novels})

    def post(self,req):
        res = {
            "status": 1,
            "error": None,
            "data": None
        }
        user_id = req.session["user_id"]
        novel_id = req.POST.get("novel_id")
        models.User_Novel.objects.create(novel_id=novel_id, user_id=user_id)
        return HttpResponse(json.dumps(res))

    def delete(self,req):
        res = {
            "status": 1,
            "error": None,
            "data": None
        }
        user_id = req.session["user_id"]
        # novel_id = req.DELETE.get("novel_id",None) #主：WSGIRequest没有PUT和DELETE属性,所以只能通过以下方式获取
        delete = QueryDict(req.body)
        novel_id = delete.get('novel_id')
        models.User_Novel.objects.filter(novel_id=novel_id,user_id=user_id).delete()
        return HttpResponse(json.dumps(res))

@login_require
def bookstore(req):
    novels = models.Novel.objects.all()
    qihuan_novels = novels.filter(novel_type=0).all().order_by("-novel_id")[:6]
    wuxia_novels = novels.filter(novel_type=1).all().order_by("-novel_id")[:6]
    doushi_novels = novels.filter(novel_type=2).all().order_by("-novel_id")[:6]
    lishi_novels = novels.filter(novel_type=3).all().order_by("-novel_id")[:6]
    kehuan_novels = novels.filter(novel_type=4).all().order_by("-novel_id")[:6]
    wangyou_novels = novels.filter(novel_type=5).all().order_by("-novel_id")[:6]
    nvsheng_novels = novels.filter(novel_type=6).all().order_by("-novel_id")[:6]
    return render(req, "novel/book_store.html", {
        "qihuan_novels": qihuan_novels,
        "wuxia_novels": wuxia_novels,
        "doushi_novels": doushi_novels,
        "lishi_novels": lishi_novels,
        "kehuan_novels": kehuan_novels,
        "wangyou_novels": wangyou_novels,
        "nvsheng_novels": nvsheng_novels
    })

@login_require
def novelDetail(req, novel_id):
    user_id = req.session["user_id"]
    bookrack_result = models.User_Novel.objects.filter(novel_id=novel_id, user_id=user_id).first()

    if bookrack_result:
        is_in_bookrack = 1
    else:
        is_in_bookrack = 0

    novel = models.Novel.objects.filter(novel_id=novel_id).first()

    chapters = None
    novel_type = novel.novel_type  # 得到类型

    novel_list = [
        novel.qihuan_chapters_set.all,  # 奇幻/玄幻
        novel.wuxia_chapters_set.all,  # 武侠/仙侠
        novel.doushi_chapters_set.all,  # 都市/言情
        novel.lishi_chapters_set.all,  # 历史/军事
        novel.kehuan_chapters_set.all,  # 科幻/灵异
        novel.wangyou_chapters_set.all,  # 网游/竞技
        novel.nvsheng_chapters_set.all  # 女生频道
    ]

    # ps查询后再切片会需要13秒的时间，所以直接切片，注意跟踪后续报错
    chapters = novel_list[novel_type]().order_by("-chapter_id")[0:10]

    if novel.novel_status == 0:
        novel_status = "连载中"
    else:
        novel_status = "已完结"

    novel_type_name_list = ["奇幻/玄幻", "武侠/仙侠", "都市/言情", "历史/军事", "科幻/灵异", "网游/竞技", "女生频道"]
    novel_type_name = novel_type_name_list[novel_type]
    last_chapter_title = chapters[0].chapter_title

    return render(req, "novel/book_detail.html", {
        "novel": novel,
        "chapters": chapters,
        "novel_type_name": novel_type_name,
        "last_chapter_title": last_chapter_title,
        "is_in_bookrack": is_in_bookrack
    })

def judge_models(novel_type):
    '''
    封装方法，此方法判定动态采用哪一个表：
    :param novel_type:小说类型 
    :return: 小说的models.obj
    '''
    chapter_data_list = [
        models.Qihuan_chapters,
        models.Wuxia_chapters,
        models.Doushi_chapters,
        models.Lishi_chapters,
        models.Kehuan_chapters,
        models.Wangyou_chapters,
        models.Nvsheng_chapters
    ]
    return chapter_data_list[novel_type]

@login_require
def catalog_page(req, novel_type, novel_id):
    database_chapter = judge_models(novel_type)
    chapter = database_chapter.objects.filter(novel_id=novel_id).first()
    return render(req, "novel/book_catalog.html", {
        "novel_type": novel_type,
        "novel_id": novel_id,
        "novel_title":chapter.novel.novel_title
    })

def catalog_data(req, novel_type, novel_id, page_num):
    '''
     这个方法返回小说的章节目录
    :param req: 必要请求参数
    :param novel_type: 小说类型
    :param novel_id: 小说的id
    :param novel_id: 目录页数
    :return: 渲染页面
    '''
    res = {
        "status": 1,
        "error": None,
        "data": None
    }
    # 获取id
    database_chapter = judge_models(novel_type)
    start_num = (page_num - 1) * page_config
    end_num = page_num * page_config - 1
    chapters = database_chapter.objects.filter(novel_id=novel_id).order_by("chapter_id")[start_num:end_num]
    data = []
    for chapter in chapters:
        chapter_content = {
            "chapter_id": chapter.chapter_id,
            "chapter_title": chapter.chapter_title
        }
        data.append(chapter_content)
    res["data"] = data
    return HttpResponse(json.dumps(res))

@login_require
def chapterContent(req,novel_type,novel_id,chapter_id):
    database_chapter = judge_models(novel_type)
    chapters = database_chapter.objects.filter(novel_id=novel_id).all().order_by("chapter_id")
    chapter = chapters.filter(chapter_id=chapter_id).first()
    next_chapter = chapters.filter(chapter_id__gt=chapter_id).first()  # 大于的第一个即下一章
    pre_chapter = chapters.filter(chapter_id__lt=chapter_id).last()  # 小说的最后一个即上一章
    pre_chapter_id=""
    next_chapter_id=""
    if pre_chapter:
        pre_chapter_id = pre_chapter.chapter_id

    if next_chapter:
        next_chapter_id = next_chapter.chapter_id

    return render(req,"novel/book_content.html",{
        "chapter_title": chapter.chapter_title,
        "content":chapter.chapter_content,
        "novel_type": novel_type,
        "novel_id": novel_id,
        "pre_chapter_id":pre_chapter_id,
        "next_chapter_id":next_chapter_id
    })

@login_require
def booksearch(req):
    '''
    处理图书请求
    :param req: 必要参数
    :return: 搜索结果渲染页面
    '''
    search_key=req.GET.get("search_key")
    novels=models.Novel.objects.filter(novel_title__contains=search_key).all()
    return render(req,"novel/book_search.html",{"novels":novels,"search_key":search_key})

