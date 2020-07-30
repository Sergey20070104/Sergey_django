from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Diary

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['diary']

    def location(self, item):
        return reverse(item)

class DiarySitemap(Sitemap):
    def items(self):
        return Diary.objects.all()

