from django.urls import path
from .views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormUpdateView


urlpatterns = [
    path('', IndexView.as_view(), name="article_index"),
    path('<int:id>/', ArticleView.as_view(), name="article_show"),
    path('create/', ArticleFormCreateView.as_view(), name="article_create"),
    path('<int:id>/edit', ArticleFormUpdateView.as_view(), name="article_update"),
]