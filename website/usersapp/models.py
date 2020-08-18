from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='profile_pictures', default='default_pic.jpg')
    locations = models.CharField(
        max_length=30, default='No location Provided....')

    def __str__(self):
        return f"{self.user.username} Account Profile"
