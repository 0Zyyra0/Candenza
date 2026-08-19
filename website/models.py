from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to='media/posts/',
        default='media/posts/default.jpg'
    )
    category = models.ManyToManyField(Category)

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title