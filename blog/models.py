from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=200)
    text_article = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField('Текст комментария')
    comment_pub_date = models.DateTimeField('Дата публикации', auto_now_add=timezone.now)
    author = models.ForeignKey(User, related_name='usernames', verbose_name='Автор комментария', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
