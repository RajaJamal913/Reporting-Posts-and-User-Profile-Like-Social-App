from django.urls import path

from django.conf import settings
from .views import upload_post, display_posts
from django.conf.urls.static import static


urlpatterns = [
    path('upload/', upload_post, name='upload_post'),
    path('display/', display_posts, name='display_posts'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
