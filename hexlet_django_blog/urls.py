from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    # path('', views.index),
    # path('', views.IndexView.as_view()),
    # path('', TemplateView.as_view(template_name='index.html')),
    # path('', IndexView.as_view(), name='index'),
    path('about/', views.about),
    path('articles/', include('hexlet_django_blog.article.urls')),
    path('admin/', admin.site.urls),
]
