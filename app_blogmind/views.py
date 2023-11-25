from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from .models import Post, UserProfile

def ViewLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            auth.login(request, user)
            return redirect('home')
        elif user is not None and not user.check_password(password):
            messages.info(request, 'Senha Incorreta')
            return redirect('login')
        else:
            messages.info(request, 'Usuário Não Existe')
            return redirect('login')

    return render(request, 'signin.html')

def ViewRegister(request):
    return render(request, 'signup.html')

@login_required(login_url='login')
def ViewLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def ViewHome(request):
    user = request.user
    """user_profile = UserProfile.objects.get(user=user)"""

    """post = Post.objects.get(user=user)"""
    
    posts = Post.objects.all()

    

    return render(request, 'blog/home.html', {'posts':posts})

@login_required(login_url='login')
def ViewDetail(request, year, month, day, slug):

    post = Post.objects.get(created__year=year, created__month=month, created__day=day, slug=slug)

    return render(request, 'detail/detail.html', {'post':post})