from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'

    def index(request, **kwargs):
        return render(request, 'index.html')

    def get_about(request, *args, **kwargs):
        return render(request, 'about.html')