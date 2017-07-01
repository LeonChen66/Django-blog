from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Post, self_intro

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# Create your views here.

def index_page(request):
    limit = 3
    intro = self_intro.objects.get(pk=1)
    post_list = Post.objects.all()[::-1]
    paginator = Paginator(post_list,limit)
    page = request.GET.get('page')  # 获取页码
    try:
        post_list = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        post_list = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        post_list = paginator.page(paginator.num_pages)  # 取最后一页的记录

    return render(request,'index.html',{
        'today': str(datetime.now().strftime('%Y-%m-%d')),
        'current_time':str(datetime.now().strftime('%H:%M:%S')),
        'post_list': post_list,
        'intro': intro,
    })


def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    intro = self_intro.objects.get(pk=1)
    return render(request,'post.html',
                  {'post':post,
                   'today': str(datetime.now().strftime('%Y-%m-%d')),
                   'current_time': str(datetime.now().strftime('%H:%M:%S')),
                   'intro': intro,
                   })

                   
def archives(request):
    post_list = Post.objects.all()[::-1]
    intro = self_intro.objects.get(pk=1)
    return render(request,'archives.html',{
        'today': str(datetime.now().strftime('%Y-%m-%d')),
        'current_time': str(datetime.now().strftime('%H:%M:%S')),
        'post_list': post_list,
        'intro': intro,
    })


def about(request):
    intro = self_intro.objects.get(pk=1)
    about = self_intro.objects.get(pk=2)
    return render(request,'about.html',{
        'today': str(datetime.now().strftime('%Y-%m-%d')),
        'current_time': str(datetime.now().strftime('%H:%M:%S')),
        'intro': intro,
        'about': about,
    })


def talks(request):
    intro = self_intro.objects.get(pk=1)
    talks = self_intro.objects.get(pk=3)
    return render(request,'talk.html',{
        'today': str(datetime.now().strftime('%Y-%m-%d')),
        'current_time': str(datetime.now().strftime('%H:%M:%S')),
        'intro': intro,
        'talks': talks,
    })
