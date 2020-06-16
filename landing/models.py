from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MyLessons(models.Model):
    name = models.CharField('Наименование', max_length=100)
    school = models.CharField('Организация', max_length=100)
    annotation = models.TextField('Аннотация')
    date_create = models.DateTimeField(default=timezone.now)
class Diary(models.Model):
    text=models.TextField('Запись')
    author=models.ForeignKey(User, on_delete=models.PROTECT)
    data=models.DateTimeField(default=timezone.now)

