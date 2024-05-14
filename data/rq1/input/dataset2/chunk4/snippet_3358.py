#Source: https://stackoverflow.com/questions/73727265/attributeerror-wsgirequest-object-has-no-attribute-is-ajax-in-django-4-hi
import random

from django.shortcuts import render
from highcharts.views import HighChartsBarView


class BarView(HighChartsBarView):
    title = 'Example Bar Chart'
    subtitle = 'my subtitle'
    categories = ['Orange', 'Bananas', 'Apples']
    chart_type = ''
    chart = {'zoomType': 'xy'}
    tooltip = {'shared': 'true'}
    legend = {'layout': 'horizontal', 'align': 'left',
              'floating': 'true', 'verticalAlign': 'top',
              'y': -10, 'borderColor': '#e3e3e3'}

    @property
    def series(self):
        result = []
        for name in ('Joe', 'Jack', 'William', 'Averell'):
            data = []

        for x in range(len(self.categories)):
            data.append(random.randint(0, 10))
        result.append({'name': name, "data": data})
        return result