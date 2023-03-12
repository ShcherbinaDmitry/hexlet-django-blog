from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages

from .models import Article
from .forms import ArticleCommentForm, ArticleForm


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        flash_messages = messages.get_messages(request)
        return render(request, 'article/index.html', context={
            'articles': articles,
            'messages': flash_messages,
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

class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        flash_messages = messages.get_messages(request)
        return render(request, 'article/create.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article has been created!')
            return redirect('article_index')
        messages.error(request, 'Couldn\'t create an article. Check form data.')
        return render(request, 'article/create.html', {'form': form})

class CommentArticleView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleCommentForm()
        return render(request, 'comment.html', {'form': form})