from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from video_downloader.views import download_video

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', download_video)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
