from django.db import models


class Blog(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  writer = models.CharField(max_length=20, default='')
  createdAt = models.DateTimeField(auto_now_add=True)
  first_name = models.CharField(max_length=20, default='') 
  last_name = models.CharField(max_length=20, default='')   
  
  
  def __str__ (self):
    return self.title
  

    

# Create your models here.
