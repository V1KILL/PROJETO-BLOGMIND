
from django.urls import path
from .views import ViewHome, ViewDetail, ViewLogin, ViewRegister, ViewLogout, ViewAccount, ViewProfile, ViewPost, ViewMudarPerfil, ViewMudarBackGround, ViewMudarNome, ViewMudarSenha, ViewComentar

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', ViewHome, name='home'),
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)