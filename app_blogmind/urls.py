
from django.urls import path
from .views import ViewHome, ViewLogin, ViewRegister, ViewLogout, ViewProfile, ViewVisitant
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', ViewHome, name='home'),
    path('login', ViewLogin, name='login'),
    path('register', ViewRegister, name='register'),
    path('logout', ViewLogout, name='logout'),
    path('visitant', ViewVisitant, name='visitant'),
    path('profile/<int:id>', ViewProfile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)