from django.contrib import admin
from .models import MyLessons

class MyLessonAdmin(admin.ModelAdmin):

    model = MyLessons
    list_display = ('name', 'school', 'annotation', 'date_create', 'id')

admin.site.register(MyLessons, MyLessonAdmin)
