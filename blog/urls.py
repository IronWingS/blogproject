from django.conf.urls import url
from . import views

# 告诉Django这个urls.py文件是属于blog这个app的，这种技术叫视图函数命名空间。	
app_name='blog'

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    # 视图函数，匹配url和视图函数，当输入该网址的时候，调用对应的视图函数，执行相应的操作，并且对该视图函数起名为index和detail。
    # 那问题来了，这个视图函数的别名有什么用？
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    # 这里没有加括号，没有将这个正则表达式当作一个命名组。
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category')
]
