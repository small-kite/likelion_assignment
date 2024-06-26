from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Blog,Comment,Tag
from .forms import BlogForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



def blog_detail(request, blog_id):
  blog = Blog.objects.get(pk=blog_id)
  likes_count = blog.likes.count()
  return render(request, 'blog/blog_detail.html', {'blog': blog, 'blog.likes.count': likes_count})


def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'page_obj':page_obj})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    comments = Comment.objects.filter(blog=blog) 
    tags = blog.tag.all() #저장된 태그 모두 불러옴
    return render(request,'detail.html',{'blog':blog, 'comments':comments, 'tags':tags})

def new(request):
    tags = Tag.objects.all()
    return render(request,'new.html',{'tags':tags})

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST.get('title')
    new_blog.content = request.POST.get('content')
    new_blog.image = request.FILES.get('image')
    new_blog.author = request.user
    new_blog.save()
    tags = request.POST.getlist('tags') #태그 전체 불러옴
    for tag_id in tags: #for문 돌면서 태그 아이디가 같은 걸 불러와서 블로그에 저장 , add이용하면 save하지않아도 저장해줌
        tag = Tag.objects.get(id=tag_id)
        new_blog.tag.add(tag)
    return redirect('detail', new_blog.id)

def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    if edit_blog.author != request.user: #자기 게시물이 아닌 게시물에 수정하기버튼 누르면 홈으로 리다이렉트
        return redirect('home')
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.image = request.FILES.get('image')
    old_blog.save()
    return redirect('detail', old_blog.id)

    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', old_blog.id)

    return render(request, 'new.html', {'old_blog':old_blog})


def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')

#댓글 생성
def create_comment(request, blog_id):
    comment = Comment()
    comment.content = request.POST.get('content')
    comment.blog = get_object_or_404(Blog,pk=blog_id) # 블로그없으면 댓글 존재하면 안됨
    comment.author = request.user
    comment.save()

    return redirect('detail',blog_id)

def new_comment(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'new_comment.html',{'blog':blog})

def like(request, blog_id):
    if request.user.is_authenticated:
        blog = get_object_or_404(Blog, pk=blog_id)
        if blog.likes.filter(pk=request.user.pk).exists():  # 수정된 부분
            blog.likes.remove(request.user)  # 수정된 부분
        else:
            blog.likes.add(request.user)  # 수정된 부분
        return redirect('detail', blog_id)
    return redirect('login')

