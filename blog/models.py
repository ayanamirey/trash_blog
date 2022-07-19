from django.contrib.auth.models import User
from django.db import models
from .middleware import get_current_user
from django.db.models import Q


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец статьи',
                               null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображения')

    def __str__(self):
        return f'{self.title}'


class StatusFilterComments(models.Manager):
    def get_queryset(self):
        user = get_current_user()
        if not user.is_authenticated:
            return super().get_queryset().filter(status=True)
        return super().get_queryset().filter(
            Q(status=False, author=user) | Q(status=False, post__author=user) | Q(status=True))


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments_posts',
                             blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария',
                               null=True, blank=True)
    text = models.TextField(verbose_name='Комментарий')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    status = models.BooleanField(default=False)
    objects = StatusFilterComments()

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return f'{self.text}'
