from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_text = models.TextField(blank=True, null=True)
    content_image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    content_video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.user.username} on {self.created_at}'
