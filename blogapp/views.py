from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
import json
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def index(request):
    search_query = ""
    if request.GET.get("keyword"):
        search_query = request.GET.get("keyword")
    print(search_query)
    blogs = Blog.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    
    page = request.GET.get("page")
    results = 4
    paginator = Paginator(blogs, results)
    
    try:
        blogs = paginator.page(page)
    
    except PageNotAnInteger:
        page = 1
        blogs = paginator.page(page)
    
    except EmptyPage:
        page = paginator.num_pages
        blogs = paginator.page(page)
    
    context = {"blogs":blogs, "search_query": search_query, "paginator": paginator}
    return render(request, "blogapp/index.html", context)

def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(blog=blog)
    
    user = request.user
    msg = None
    if blog.likes.filter(id=user.id).exists():
        msg = "yes"
    else:
        msg = None
    context = {"blog": blog, "msg": msg, "comments": comments}
    return render(request, "blogapp/detail.html", context)

def like_blog(request):
    data = json.loads(request.body)
    blog_id = data["id"]
    user = request.user
    blog = Blog.objects.get(id = blog_id)
    msg = None
    
    if blog.likes.filter(id=user.id).exists():
        print("please unlike biko")
        blog.likes.remove(user)
        msg = {
            "like": "no",
            "num": blog.likes.count()
        }
    
    else:
        print("like it biko")
        blog.likes.add(user)
        msg = {
            "like": "yes",
            "num": blog.likes.count()
        }
    return JsonResponse(msg, safe=False)


def addComment(request):
    data = json.loads(request.body)
    blog_id = data["id"]
    comment = data["comment"]
    blog = Blog.objects.get(id=blog_id)
    new_comment = Comment.objects.create(body=comment, user=request.user.username, blog=blog)
    data = {
        "body": new_comment.body,
        "user": new_comment.user
    }
    
    return JsonResponse(data, safe=False)