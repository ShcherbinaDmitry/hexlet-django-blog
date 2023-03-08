from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'

    def index(request, **kwargs):
        return redirect(reverse('article', kwargs= { 'tags': 'python', 'article_id': 42 }))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Dima!'

        return context

    def get_about(request, *args, **kwargs):
        return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')