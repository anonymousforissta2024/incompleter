#Source: https://stackoverflow.com/questions/57515323/attributeerror-tuple-object-has-no-attribute-get
class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'instructor/course_update_form.html'
    success_url = reverse_lazy('instructor:course:list')
    success_message = 'Se modificó con éxito el curso "{}".'

    def get_form(self, form_class = None):
        if form_class is None:
            form_class = self.get_form_class()

        form = form_class(**self.get_form_kwargs(), title_valid = True)
        for field in form.fields.keys():
            form.fields[field].required = False

        return form

    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.slug = slugify(obj.title)
        obj.save()

        messages.success(self.request, self.success_message.format(obj.title))
        return redirect(self.success_url)