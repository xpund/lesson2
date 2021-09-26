from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    pub_date = models.DateTimeField('Дата публикации', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'