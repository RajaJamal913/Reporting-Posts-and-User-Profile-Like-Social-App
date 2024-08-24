from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', views.view_profile, name='view_profile'),  # To view all profiles
    path('profile/<int:user_id>/', views.view_profile, name='view_profile'),  # T
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
