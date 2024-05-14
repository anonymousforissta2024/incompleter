#Source: https://stackoverflow.com/questions/49818728/typeerror-metaclass-conflict-python-3-django-2
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin


class MainPageView(TemplateView, CategoryListMixin):
    template_name = 'mainpage.html'