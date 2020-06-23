from django.urls import path
from django.views.generic.base import TemplateView
from .views import MyLessonsView,DiaryView,MyLessonsDetailView


urlpatterns = [
    path('', MyLessonsView.as_view(
        template_name="landing/index.html"
    ), name='home'),
    path('about/', TemplateView.as_view(
        template_name="landing/about.html"
    ), name='about'),
    path('contact/', TemplateView.as_view(
        template_name="landing/contact.html"
    ), name='contact'),
    path('project/', TemplateView.as_view(
        template_name="landing/project.html"
    ), name='project'),
    path('diary/', DiaryView.as_view(), name='diary'),
    path('<int:pk>/', MyLessonsDetailView.as_view(), name='mylesson-detail'),

]