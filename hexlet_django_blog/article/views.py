from django.shortcuts import render, get_object_or_404
from django.views import View

from hexlet_django_blog.article.models import Article
from .forms import ArticleCommentForm

# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'article/index.html', context={
            'articles': articles
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'article/show.html', context={
            'article': article
        })
    
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # comment.content = check_for_spam(form.data['content']) - process model
            comment.save()


class CommentArticleView(View):
    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()
        return render(request, 'comment.html', {'form': form})