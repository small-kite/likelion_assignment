
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth

#회원가입

def signup(request):
  if request == "POST":
    if request.POST['password1'] == request.POST['password2']:
      user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password1'],
        email=request.POST['email'],)
      
      
      profile = Profile(
        user=user,
        nickname=request.POST['nickname'],
        image=request.FILES.get('profile_image'),)
      
      profile.save()   #객체 생성 후 DB에 반영
      auth.login(request, user)
      return redirect('home')
    return render(request, 'signup.html') # type: ignore #비밀번호가 일치 하지 않는 경우 가입하기로 돌아가기
  return render(request, 'signup.html') # type: ignore #POST 요청이 아닌 다른 요청이 오는 경우 가입하기로 돌아가기
      
#로그인
def login(request):
   if  request.method == 'POST':
     username = request.POST['username']
     password = request.POST['password']
     user = authenticate(request, username=username, password=password)
     if user is not None:  #None은 기존회원정보가 없는 것
       auth.login(request, user)
       return redirect('home')
     return render(request, 'login.html') # type: ignore #None인 경우 로그인으로 돌아가기 
   return render(request, 'login.html') # type: ignore #POST요청이 아닌 경우 
      
      
#로그아웃
def logout(request):
  auth.logout(request)
  return redirect('home')