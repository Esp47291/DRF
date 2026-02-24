from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('materials.urls')),      # маршруты курсов и уроков
    path('api/', include('users.urls')),          # маршруты пользователей и платежей
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)