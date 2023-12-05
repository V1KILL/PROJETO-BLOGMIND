from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from .models import Post, UserProfile, Comment
from django.shortcuts import get_object_or_404

from taggit.models import Tag

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
    posts = Post.objects.all().exclude(user=UserProfile.objects.get(user=request.user))
    
                                   
    return render(request, 'blog/home.html', {'posts':posts})

@login_required(login_url='login')
def ViewDetail(request, year, month, day, slug):
    post = Post.objects.get(created__year=year, created__month=month, created__day=day, slug=slug)
    comments = post.comments.all()

    return render(request, 'detail/detail.html', {'post':post, 'comments':comments})

@login_required(login_url='login')
def ViewPost(request):
    user = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        title = request.POST['title']
        descricao = request.POST['descricao']
        tags = request.POST['tags']
        
        if 'file' in request.FILES:
            arquivo = request.FILES['file']
            
            post = Post.objects.create(user=user, title=title, description=descricao, image=arquivo)

            post.tags.add(*tags)
            return redirect('profile', request.user.id)
       

    return render(request, 'postar.html', {'user':user})

@login_required(login_url='login')
def ViewMudarPerfil(request):
    if request.method == 'POST':
        image = request.FILES['image']
        user = UserProfile.objects.get(user=request.user)
        user.profileimg = image
        user.save()
    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)
 
@login_required(login_url='login')
def ViewMudarBackGround(request):
    if request.method == 'POST':
        image = request.FILES['image']
        user = UserProfile.objects.get(user=request.user)
        user.background = image
        user.save()
    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

@login_required(login_url='login')
def ViewMudarNome(request, username):        
    url_anterior = request.META.get('HTTP_REFERER')
    
    if User.objects.filter(username=username).exists():
        
        return redirect(url_anterior)
    else:
        request.user.username = username
        request.user.save()
    return redirect(url_anterior)

@login_required(login_url='login')
def ViewMudarSenha(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        request.user.set_password(password)
        request.user.save()
        update_session_auth_hash(request, request.user)
    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

def ViewComentar(request, year, month, day, slug):
    if request.method == 'POST':
        text = request.POST['comentario']

        post = Post.objects.get(created__year=year, created__month=month, created__day=day, slug=slug)
        user = UserProfile.objects.get(user=request.user
                                       )
        
        comment = Comment.objects.create(post=post, user=user, text=text)

    url_anterior = request.META.get('HTTP_REFERER')
    return redirect(url_anterior)

def ViewTag(request, tag_slug=None):
    posts = Post.objects.all().exclude(user=UserProfile.objects.get(user=request.user))
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = posts.filter(tags__in=[tag])

    return render(request, 'blog/home.html', {'posts':posts})

def ViewEditPost(request, year, month, day, slug):
    return redirect('/')

def ViewRemovePost(request, year, month, day, slug):
    post = Post.objects.get(user=UserProfile.objects.get(user=request.user),created__year=year, created__month=month, created__day=day, slug=slug)
    post.delete()
    return redirect('/')

def ViewShare(request, year, month, day, slug):
    return redirect('/')

def ViewInfo(request, year, month, day, slug):
    return redirect('/')