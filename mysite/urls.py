from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls', namespace='blog')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
