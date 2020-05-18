from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(default='')
    category = models.CharField(max_length=10)
    time = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title