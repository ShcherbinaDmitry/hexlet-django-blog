from django.urls import path
from hexlet_django_blog.article.views import ArticleView


urlpatterns = [
    path('', ArticleView.as_view()),
]