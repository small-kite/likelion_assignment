from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate
from .models import Profile
from django.contrib import auth #auth들어간 것은 인증에 관련된 것
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from users.models import User

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if not username:
            return render(request, 'signup.html', {'error': 'Username is required'})
          
        if Profile.objects.filter(user__username=username).exists():
          return render(request, 'signup.html', {'error': 'Username already exists'})

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=request.POST['password1'],
                    email=request.POST['email'],
                )
                profile = Profile.objects.create(
                    user=user,
                    gender=request.POST['gender'],
                    nickname=request.POST['nickname'],
                    introduction=request.POST['introduction'],
                    image=request.FILES.get('image')
                )
                return redirect('login')  # Redirect to login page after signup
            except IntegrityError:
                # Handle IntegrityError if any other unique constraint fails
                return render(request, 'signup.html', {'error': 'An error occurred'})
        else:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'signup.html')
def login(requst):
    if requst.method == 'POST' :
        username = requst.POST['username']
        password = requst.POST['password']
        user = authenticate(requst, username=username, password=password) #장고한테 일치하는지 확인해주라고 요청

        if user is not None:
            auth.login(requst, user)
            return redirect('home') # user가 None이 아니면(=정상적인 로그인) home으로 리다이렉트
        return render(requst, template_name='login.html') #user가 None이면 회원정보 없거나 오류라서 다시 로그인화면 뿌려줌
    return render(requst, template_name='login.html')# POST요청이 아니어도 로그인화면 보여줌
def logout(request):
    auth.logout(request)
    return redirect('home')
        
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required

@login_required
def profile_base(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile, created = Profile.objects.get_or_create(user=user)
    context = {'profile_user': user, 'profile_type': 'base', 'profile': profile}
    return render(request, 'profile/profile_base.html', context)

@login_required 
def profile_edit(request, user_id):
    if request.method == 'POST':
        # POST 요청 처리
        user = get_object_or_404(User, pk=user_id)
        if request.user != user:  
            return render(request, 'error.html', {'message': '권한이 없습니다.'})  
        profile = user.profile  
        profile.gender = request.POST['gender']
        profile.introduction = request.POST['introduction']
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
        profile.save()
        return redirect('users:profile_base', user_id=user_id)  
    else:
        # GET 요청 처리
        user = get_object_or_404(User, pk=user_id)
        if request.user != user:  
            return render(request, 'error.html', {'message': '권한이 없습니다.'})  
        profile = user.profile  
        context = {'profile': profile}
        return render(request, 'profile/profile_edit.html', context)