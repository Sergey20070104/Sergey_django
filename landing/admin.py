from django.contrib import admin
from .models import MyLessons,Diary

class MyLessonAdmin(admin.ModelAdmin):

    model = MyLessons
    list_display = ('name', 'school', 'annotation', 'date_create', 'id')
class DiaryAdmin(admin.ModelAdmin):
    model=Diary
    list_display = ('text','author','data')

admin.site.register(MyLessons, MyLessonAdmin)
admin.site.register(Diary, DiaryAdmin)
