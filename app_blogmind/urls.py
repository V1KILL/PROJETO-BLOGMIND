
from django.urls import path
from .views import ViewHome, ViewDetail, ViewLogin, ViewRegister, ViewLogout, ViewAccount, ViewProfile, ViewPost, ViewMudarPerfil, ViewMudarBackGround, ViewMudarNome, ViewMudarSenha, ViewComentar, ViewTag, ViewRemovePost, ViewInfo, ViewShare, ViewEditPost

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', ViewHome, name='home'),
    path('tag/<slug:tag_slug>/', ViewTag, name='tag'),
    path('login', ViewLogin, name='login'),
    path('register', ViewRegister, name='register'),
    path('logout', ViewLogout, name='logout'),
    path('account', ViewAccount, name='account'),
    path('profile/<int:id>', ViewProfile, name='profile'),
    path('postar', ViewPost, name='postar'),
    path('comentar/<int:year>/<int:month>/<int:day>/<str:slug>', ViewComentar, name='comentar'),
    path('mudarperfil', ViewMudarPerfil, name='mudarperfil'),
    path('mudarbackground', ViewMudarBackGround, name='mudarbackground'),
    path('mudarnome/<str:username>', ViewMudarNome, name='mudarnome'),
    path('mudarsenha', ViewMudarSenha, name='mudarsenha'),
    path('detail/<int:year>/<int:month>/<int:day>/<str:slug>', ViewDetail, name='detail'),
    path('removepost/<int:year>/<int:month>/<int:day>/<str:slug>', ViewRemovePost, name='removepost'),
    path('editpost/<str:titulo>/<str:descricao>/<int:id>', ViewEditPost, name='editpost'),
    path('share/<int:year>/<int:month>/<int:day>/<str:slug>', ViewShare, name='share'),
    path('info/<int:year>/<int:month>/<int:day>/<str:slug>', ViewInfo, name='info'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)