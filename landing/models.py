from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify


class MyLessons(models.Model):
    name = models.CharField('Наименование', max_length=100)
    school = models.CharField('Организация', max_length=100)
    annotation = models.TextField('Аннотация')
    date_create = models.DateTimeField(default=timezone.now)
class Diary(models.Model):
    text=models.TextField('Запись')
    author=models.ForeignKey(User, on_delete=models.PROTECT)
    data=models.DateTimeField(default=timezone.now)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}'


class Record(models.Model):
    name = models.CharField('Номер робота', max_length=100)
    temp = models.FloatField(default=0)
    mass = models.FloatField(default=0)
    quality=models.FloatField(default=0)
    ip=models.CharField(default='',max_length=100)
    date_create = models.DateTimeField(default=timezone.now)

