from django.urls import path

from hexlet_django_blog.article import views

# urlpatterns = [
#     path('', views.index),
# ]

from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
