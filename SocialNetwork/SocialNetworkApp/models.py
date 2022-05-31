from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'