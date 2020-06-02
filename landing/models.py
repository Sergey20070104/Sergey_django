from django.db import models
from django.utils import timezone

class MyLessons(models.Model):
    name = models.CharField('Наименование', max_length=100)
    school = models.CharField('Организация', max_length=100)
    annotation = models.TextField('Аннотация')
    date_create = models.DateTimeField(default=timezone.now)


