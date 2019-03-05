#-*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views

# 此类可以定义admin后台显示的字段，比如文章列表显示标题，创建时间，
class PostAdmin(object):
    # 展示的字段
    list_display = ['id','title','created_time','category']
    # 按文章名进行搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['id','title','created_time','category']
    # 修改图标
    model_icon = 'fa fa-bell'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['']

    # 不显示某一字段
    exclude = ['']

    # style_fields = {'body':'ueditor'}

class CategoryAdmin(object):
    list_display = ['id','name']
    search_fields = ['name']
    # list_filter = ['name']
    model_icon = 'fa fa-briefcase'

class TagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-tags'



# admin.site.register(Article, admin_class=ArticleAdmin)

xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)

# 修改xadmin的基础配置
class BaseSetting(object):
    # 允许使用主题
    enable_themes = True
    use_bootswatch = True

# 修改xadmin的全局配置
class GlobalSetting(object):
    site_title = '向东的笔记本'
    site_footer = '2019'

    # Models收起功能
    # menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting )