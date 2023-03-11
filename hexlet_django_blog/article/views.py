from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View

# Create your views here.

def index(request, tags, article_id):
    return render(request, 'article.html', context={
        'tags': tags,
        'article_id': article_id,
    })

class ArticleView(View):
    def index(self, request, *args, **kwargs):
        return render(request, 'article.html', context={
            'app_name': 'article'
        })