from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView
from .models import MyLessons,Record
from django.views.generic.edit import CreateView
from .forms import DiaryForm
from .models import Diary
from django.contrib.messages.views import SuccessMessageMixin


class MyLessonsView(ListView):
    model = MyLessons
    template_name = 'landing/index.html'
    paginate_by = 2
class DiaryView(CreateView,ListView):
    form_class = DiaryForm
    success_url = '/'
    template_name = 'landing/diary.html'
    model=Diary

class MyLessonsDetailView(DeleteView):
    model = MyLessons
    template_name = 'landing/detail_lesson.html'
    context_object_name = 'Lesson'
class RecordView(ListView):
    model = Record
    template_name = 'landing/record.html'
    paginate_by = 2
class DiaryUpdate(SuccessMessageMixin,UpdateView):
    model = Diary
    fields = ['text']
    template_name = 'landing/diary_update.html'
    success_url = '/diary'
    success_message = "Запись сохранена!"
class DiaryDelete(SuccessMessageMixin, DeleteView):
    model = Diary
    template_name = 'landing/diary_delete.html'
    success_url = '/diary'
    success_message = "Запись удалена!"



