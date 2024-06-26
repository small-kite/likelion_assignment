from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  #주로 하나로 맞추기 
  nickname = models.CharField(max_length=10, null=True)
  image = models.ImageField(upload_to='profile/', null=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author')

  
  class Meta:
    db_table = 'profile'
    
  def __str__(self):
    return self.nickname
  
  def summary(self):
    return self.content[:100]
                        
