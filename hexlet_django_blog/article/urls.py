from django.urls import path
from .views import IndexView, ArticleView, ArticleFormCreateView


urlpatterns = [
    path('', IndexView.as_view(), name="article_index"),
    path('<int:id>/', ArticleView.as_view(), name="article_show"),
    path('create/', ArticleFormCreateView.as_view(), name="article_create")
]