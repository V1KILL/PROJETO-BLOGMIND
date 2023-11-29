from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from .models import Post, UserProfile
from django.shortcuts import get_object_or_404

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Nome Existente')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                UserProfile.objects.create(user=user)

                messages.info(request, 'Conta Criada com Sucesso')


                return redirect('login')
        else:
            messages.info(request, 'Senhas não coincidem')
            return redirect('register')
    else:
        return render(request, 'signup.html')

@login_required(login_url='login')
def ViewLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def ViewAccount(request):
    user = UserProfile.objects.get(user=request.user)

    return render(request, 'account/account.html', {'user':user})

def ViewProfile(request, id):
    user = UserProfile.objects.get(user=id)

    posts = Post.objects.filter(user=user)
    return render(request, 'profile/profile.html',{'user':user, 'posts':posts})

@login_required(login_url='login')
def ViewHome(request):
    posts = Post.objects.all()
    
                                   
    return render(request, 'blog/home.html', {'posts':posts})

@login_required(login_url='login')
def ViewDetail(request, year, month, day, slug):
    post = Post.objects.get(created__year=year, created__month=month, created__day=day, slug=slug)
    comments = post.comments.all()

    return render(request, 'detail/detail.html', {'post':post, 'comments':comments})

def ViewPost(request):
    return render(request, 'postar.html')