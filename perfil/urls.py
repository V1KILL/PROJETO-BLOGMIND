from django.urls import path
from app_blogmind.views import ViewAccount, ViewMudarPerfil, ViewMudarBackGround, ViewMudarNome, ViewMudarSenha
urlpatterns = [
    path('account', ViewAccount, name='account'),
    path('mudarperfil', ViewMudarPerfil, name='mudarperfil'),
    path('mudarbackground', ViewMudarBackGround, name='mudarbackground'),
    path('mudarnome/<str:username>', ViewMudarNome, name='mudarnome'),
    path('mudarsenha', ViewMudarSenha, name='mudarsenha'),
]