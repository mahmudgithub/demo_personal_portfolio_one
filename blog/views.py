from django.shortcuts import render, get_object_or_404
from.models import Blog

def all_blog(request):
    blog_cout=Blog.objects.count
    context=Blog.objects.order_by('-date')[0:5]
    return render(request,'blog/all_blog.html',{'sos':context})

def detail(request,blog_id):
    context=get_object_or_404(Blog,pk=blog_id)
    return render (request,'blog/detail.html',{'sos':context})


