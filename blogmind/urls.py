from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_blogmind.urls')),
    path('', include('perfil.urls')),
    path('', include('post.urls')),
]

handler404 = 'app_blogmind.views.error404'

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)