from django.shortcuts import render
from django.views.generic import ListView
from .models import MyLessons

class MyLessonsView(ListView):
    model = MyLessons
    template_name = 'landing/index.html'
