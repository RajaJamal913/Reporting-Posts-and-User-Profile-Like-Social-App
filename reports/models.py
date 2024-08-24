from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from userprofile.models import UserProfile

class PostReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)  # User who reported
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        post_id = self.post.id if self.post else 'None'
        return f'Report by {self.user.username} on Post {self.post.id}'

class UserProfileReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who reported
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Increment report count and check for ban
        self.user_profile.report_count += 1
        self.user_profile.check_and_ban()
        self.user_profile.save()


    def __str__(self):
        return f'Report by {self.user.username} on User Profile {self.user_profile.id}'
