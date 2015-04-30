from django.contrib import admin

from reply import *
from ready_work import *
from memorial import *
from static_page import *
from order import *
from seo_article import *
from category import *
from service_page import *

from stonegarant.models import *

admin.site.register(Order, OrderAdmin)
admin.site.register(SeoArticle, SeoArticleAdmin)
admin.site.register(ReadyWork, ReadyWorkPageAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
admin.site.register(ServicePage, ServicePageAdmin)
admin.site.register(Memorial, MemorialPageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reply, ReplyAdmin)