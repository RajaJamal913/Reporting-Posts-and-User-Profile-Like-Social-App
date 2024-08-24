from django.urls import path
from .views import render_success, report_post
from . import views
urlpatterns = [
    path('report/<int:post_id>/', report_post, name='report_post'),
     path('report/success/', render_success, name='report_success'),
      path('accept_report/<int:report_id>/', views.accept_report, name='accept_report'),
    path('reject_report/<int:report_id>/', views.reject_report, name='reject_report'),
    path('reports/accept_user_profile/<int:report_id>/', views.accept_user_profile_report, name='accept_user_profile_report'),
    path('reports/reject_user_profile/<int:report_id>/', views.reject_user_profile_report, name='reject_user_profile_report'),  
      path('report/user_profile/<int:user_profile_id>/', views.report_user_profile, name='report_user_profile'),
]
