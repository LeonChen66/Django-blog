from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    #class Meta:  #按时间下降排序
     #   ordering = ['created_at']

class self_intro(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    def __str__(self):
        return self.title