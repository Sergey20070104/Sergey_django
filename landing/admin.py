from django.contrib import admin
from .models import MyLessons,Diary,Record

class MyLessonAdmin(admin.ModelAdmin):

    model = MyLessons
    list_display = ('name', 'school', 'annotation', 'date_create', 'id')
class DiaryAdmin(admin.ModelAdmin):
    model=Diary
    list_display = ('text','author','data')
class RecordAdmin(admin.ModelAdmin):
    model=Record
    list_display = ('name','temp','mass','quality','ip','date_create')
admin.site.register(MyLessons, MyLessonAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Record, RecordAdmin)
