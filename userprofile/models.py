
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    report_count = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    ban_end_date = models.DateTimeField(null=True, blank=True)

    def ban_for_one_month(self):
        self.is_banned = True
        self.ban_end_date = timezone.now() + timedelta(days=30)
        self.save()

    def lift_ban(self):
        self.is_banned = False
        self.ban_end_date = None
        self.save()

    def check_and_ban(self):
        if self.report_count >= 3:
            self.ban_for_one_month()

    def __str__(self):
        return self.user.username
