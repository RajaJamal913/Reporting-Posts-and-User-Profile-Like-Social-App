from django.contrib import admin
from .models import PostReport
from posts.models import Post  # Assuming your Post model is in the 'posts' app

class PostReportAdmin(admin.ModelAdmin):
    list_display = (
        'user_username',        # Username of the user who reported
        'post_id',              # ID of the reported post
        'post_creator',         # Username of the user who created the post
        'get_post_content',     # Content of the post
        'reason',               # Reason for reporting
        'created_at',           # When the report was created
    )
    search_fields = ('user__username', 'post__user__username', 'post_id', 'reason')
    list_filter = ('created_at', 'user__username')
    ordering = ('-created_at',)

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Reported By'

    # Safely retrieve the username of the user who created the post
    def post_creator(self, obj):
        try:
            post = Post.objects.get(id=obj.post_id)
            return post.user.username  # Assuming 'user' is a ForeignKey in Post
        except Post.DoesNotExist:
            return "Post not found"
        except AttributeError:
            return "User not found"
    post_creator.short_description = 'Post Creator'

    # Safely retrieve the post content
    def get_post_content(self, obj):
        try:
            post = Post.objects.get(id=obj.post_id)
            return post.content_text or "No content available"  # Assuming content_text field exists in Post model
        except Post.DoesNotExist:
            return "Post not found"
        except AttributeError:
            return "Content not found"
    get_post_content.short_description = 'Post Content'
    
    actions = ['accept_report', 'reject_report']

    def accept_report(self, request, queryset):
        for report in queryset:
            try:
                post = Post.objects.get(id=report.post_id)
                post.delete()  # Delete the reported post
            except Post.DoesNotExist:
                pass
            report.delete()  # Delete the report after processing
        self.message_user(request, "Selected reports have been accepted and posts deleted.")
    
    def reject_report(self, request, queryset):
        for report in queryset:
            report.delete()  # Delete the report after processing
        self.message_user(request, "Selected reports have been rejected and removed.")

admin.site.register(PostReport, PostReportAdmin)

from django.contrib import admin
from .models import UserProfileReport
from userprofile.models import UserProfile  # Assuming your UserProfile model is in the 'userprofile' app

class UserProfileReportAdmin(admin.ModelAdmin):
    list_display = (
        'user_username',           # Username of the user who reported
        'user_profile_id',         # ID of the reported user profile
        'reported_user_username',  # Username of the user who owns the profile
        'reason',                  # Reason for reporting
        'created_at',              # When the report was created
    )
    search_fields = ('user__username', 'user_profile__user__username', 'reason')
    list_filter = ('created_at', 'user__username')
    ordering = ('-created_at',)

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Reported By'

    # Safely retrieve the username of the user who owns the profile
    def reported_user_username(self, obj):
        try:
            user_profile = UserProfile.objects.get(id=obj.user_profile_id)
            return user_profile.user.username  # Assuming 'user' is a ForeignKey in UserProfile
        except UserProfile.DoesNotExist:
            return "User profile not found"
        except AttributeError:
            return "User not found"
    reported_user_username.short_description = 'Profile Owner'

    actions = ['accept_report', 'reject_report']

    def accept_report(self, request, queryset):
        for report in queryset:
            try:
                user_profile = UserProfile.objects.get(id=report.user_profile_id)
                user_profile.delete()  # Delete the reported user profile
            except UserProfile.DoesNotExist:
                pass
            report.delete()  # Delete the report after processing
        self.message_user(request, "Selected reports have been accepted and profiles deleted.")
    
    def reject_report(self, request, queryset):
        for report in queryset:
            report.delete()  # Delete the report after processing
        self.message_user(request, "Selected reports have been rejected and removed.")

admin.site.register(UserProfileReport, UserProfileReportAdmin)
