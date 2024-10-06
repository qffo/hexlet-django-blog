from django.shortcuts import render


# def index(request):
#     return render(request, 'article/index.html', context={
#         'who': 'article',
#     })

from hexlet_django_blog.article.models import Article
from django.views import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })
