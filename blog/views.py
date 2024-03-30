

from django.shortcuts import  render, get_object_or_404, redirect
from .models import Blog
from django.http import HttpResponse

def home(request):
  blog = Blog.objects.all()
  return render(request, 'home.html', {'blogs':blog})  

def detail(request, blog_id):
  blog = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'detail.html', {'blog':blog})

def new(request):
  return render(request, 'new.html')

def create(request):
  new_blog = Blog()
  new_blog.title=request.POST['title']
  new_blog.content=request.POST['content']
  new_blog.save()
  return redirect('detail', new_blog.id)
  
  

