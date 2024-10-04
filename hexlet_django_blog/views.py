# hexlet_django_blog/views.py
from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.http import HttpResponse
from django.views import View


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World',
#     })


def about(request):
    return render(request, 'about.html')
