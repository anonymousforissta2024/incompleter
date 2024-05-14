#Source: https://stackoverflow.com/questions/48454398/typeerror-at-en-object-of-type-proxy-is-not-json-serializable
class Index(BreadcrumbMixin, TemplateView):
    template_name = 'crud/index.html'
    index = True
    url_name = 'index' # Name argument used in urls.py
    verbose_name = _('Index')