from django.urls import path
from app_blogmind.views import ViewDetail, ViewPost, ViewComentar, ViewRemovePost, ViewEditPost, ViewSearch, ViewTag
urlpatterns = [
    path('postar', ViewPost, name='postar'),
    path('detail/<int:year>/<int:month>/<int:day>/<str:slug>', ViewDetail, name='detail'),
    path('editpost/<str:titulo>/<str:descricao>/<int:id>', ViewEditPost, name='editpost'),
    path('removepost/<int:year>/<int:month>/<int:day>/<str:slug>', ViewRemovePost, name='removepost'),
    path('comentar/<int:year>/<int:month>/<int:day>/<str:slug>', ViewComentar, name='comentar'),
    path('search', ViewSearch, name='search'),
    path('tag/<slug:tag_slug>/', ViewTag, name='tag'),
]