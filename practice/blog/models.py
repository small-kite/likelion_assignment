from django.db import models
from django.conf import settings
from users.models import User 


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)
    tag = models.ManyToManyField('Tag', blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_blogs', blank=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]

class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', default=1)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.content + ' | ' + str(self.author)
