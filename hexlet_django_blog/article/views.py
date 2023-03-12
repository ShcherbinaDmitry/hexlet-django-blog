from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article

# Create your views here.
class ArticleView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        print(articles)
        return render(request, 'article/index.html', context={
            'articles': articles
        })