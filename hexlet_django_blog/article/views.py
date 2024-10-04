from django.shortcuts import render


# def index(request):
#     return render(request, 'article/index.html', context={
#         'who': 'article',
#     })


from django.views import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'who': 'article22223333',
        }
        return render(request, 'article/index.html', context=context)
