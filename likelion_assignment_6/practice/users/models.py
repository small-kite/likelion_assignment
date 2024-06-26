from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    GENDER_CHOICES = (
        ('male', '남자'),
        ('female', '여자'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')  
    # default=1
    nickname = models.CharField(max_length=10, null=True)
    introduction = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile/', null=True)

    def __str__(self):
        return f"{self.user.username}의 프로필"

    class Meta:
        db_table = 'profile'
