from django.urls import path
from django.views.generic.base import TemplateView
from .views import MyLessonsView,DiaryView,MyLessonsDetailView,RecordView, DiaryDelete,DiaryUpdate
from .sitemaps import StaticViewSitemap, DiarySitemap
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
    'diary' : DiarySitemap,
}


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
    path('record/', RecordView.as_view(
        template_name="landing/record.html"
    ), name='record'),
    path('<int:pk>/update/', DiaryUpdate.as_view(), name='blog_update'),
    path('<int:pk>/delete/', DiaryDelete.as_view(), name='blog_delete'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

]