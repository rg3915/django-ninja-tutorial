from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    title = models.CharField('título', max_length=100)
    description = models.TextField('descrição', null=True, blank=True)
    due_date = models.DateField('data', null=True, blank=True)
    is_done = models.BooleanField('pronto', default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='usuário',
        related_name='todos',
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'todo'
        verbose_name_plural = 'todos'

    def __str__(self):
        return self.title
