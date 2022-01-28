from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = models.TextField()
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        return reverse('blog:details', args=[str(self.pk)])
