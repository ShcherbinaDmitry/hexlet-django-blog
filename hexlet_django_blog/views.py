from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Dima!'

        return context

    def get_about(self, request, *args, **kwargs):
        return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')