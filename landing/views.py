from django.shortcuts import render
from django.views.generic import ListView
from .models import MyLessons
from django.views.generic.edit import CreateView
from .forms import DiaryForm
from .models import Diary

class MyLessonsView(ListView):
    model = MyLessons
    template_name = 'landing/index.html'
class DiaryView(CreateView,ListView):
    form_class = DiaryForm
    success_url = '/'
    template_name = 'landing/diary.html'
    model=Diary
