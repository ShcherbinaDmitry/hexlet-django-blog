from django.urls import path
from .views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormUpdateView, ArticleFormDestroyView


urlpatterns = [
    path('', IndexView.as_view(), name="article_index"),
    path('create/', ArticleFormCreateView.as_view(), name="article_create"),
    path('<int:id>/edit/', ArticleFormUpdateView.as_view(), name="article_update"),
    path('<int:id>/delete/', ArticleFormDestroyView.as_view(), name="article_delete"),
    path('<int:id>/', ArticleView.as_view(), name="article_show"),
]