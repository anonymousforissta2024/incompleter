#Source: https://stackoverflow.com/questions/63129918/nameerror-name-jsonresponsemixin-is-not-defined
from programs.models import Program
from django.views.generic import ListView, DetailView

from django.http import JsonResponse
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.detail import BaseDetailView




class ProgramListView(ListView, JSONResponseMixin, SingleObjectTemplateResponseMixin):
    
    model = Program
    template_name = 'programs/program_list.html'
    context_object_name = 'programs'
    paginate_by = 6
    paginate_orphans = 3

    def get_queryset(self):

        url_parameter = self.request.GET.get('q')

        # if self.request.method == 'GET' and self.request.is_ajax():
        if self.request.method == 'GET':
            queryset = Program.objects.filter(degree = url_parameter)
            return queryset

        if self.request.method == 'GET' and url_parameter is None:
            queryset = Program.objects.all()
            return queryset


    def render_to_response(self, context, url_parameter='BSc'):
        # Look for a 'format=json' GET argument
        # if self.request.GET.get('format') == 'json':
        # if self.request.is_ajax():
        if url_parameter=='BSc':
            return self.render_to_json_response(context)
        else:
            return super().render_to_response(context)