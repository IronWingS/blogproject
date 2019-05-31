
# Create your views here.
import markdown
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from comments.forms import CommentForm

# 这些视图函数都有参数，名称为request，这个request有什么意义？参数是怎么传进来的？
# 是Django帮我们配置好的，HttpRequest请求。
def index(request):
    post_list = Post.objects.all()
    # 调用index的视图函数的时候，接受一个httprequest请求，然后会返回一个index的页面，同时为这个页面返回一个context的参数
    return render(request,'blog/index.html',context={'post_list':post_list })

def detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                              'markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    
    context =  {'post':post,
                'form':form,
                'comment_list':comment_list}
    return render(request, 'blog/detail.html',context=context)

def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year = year,
                                    created_time__month = month,
                                   )
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request, pk):
    cate = get_object_or_404(Category,pk=pk)
    # object没加s，category首字母大写了，犯了这两处错误。汗颜💧
    post_list = Post.objects.filter(category=cate)
    return render(request,'blog/index.html',context={'post_list':post_list})
        
    

