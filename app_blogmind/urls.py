
from django.urls import path
from .views import ViewHome, ViewDetail, ViewLogin, ViewRegister, ViewLogout
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login', ViewLogin, name='login'),
    path('register', ViewRegister, name='register'),
    path('logout', ViewLogout, name='logout'),
    path('home', ViewHome, name='home'),
    path('detail', ViewDetail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)