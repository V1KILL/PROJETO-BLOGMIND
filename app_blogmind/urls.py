
from django.urls import path
from .views import ViewHome, ViewDetail, ViewLogin, ViewRegister, ViewLogout
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login', ViewLogin, name='login'),
    path('register', ViewRegister, name='register'),
    path('logout', ViewLogout, name='logout'),
    path('home', ViewHome, name='home'),
    path('detail/<int:year>/<int:month>/<int:day>/<str:slug>', ViewDetail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)