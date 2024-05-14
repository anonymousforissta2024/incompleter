#Source: https://stackoverflow.com/questions/49818728/typeerror-metaclass-conflict-python-3-django-2
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import ContextMixin


class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_url'] = self.request.path
        return context

class MainPageView(TemplateView, CategoryListMixin):
    template_name = 'mainpage.html'