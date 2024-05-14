#Source: https://stackoverflow.com/questions/54966674/python-typeerror-object-of-type-user-is-not-json-serializable-after-upgrading
class TagView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.TagForm

    def post(self, request, *args, **kwargs):
        try:
            post_data = request.POST.copy()
            post_data.update({'user': request.user.pk})
            print(post_data.values)
            form = forms.TagForm(post_data)
            if form.is_valid():
                tag = form.save(commit=False)
                tag.user = request.user
                tag.email = request.user.email
                tag.save()
                request.session['user'] = tag.user
                request.session['email'] = tag.email
            else:
                print(form.errors)
                return HttpResponse(form.errors, status=400)

            print('going to redirect after successful tagging.')
            return HttpResponseRedirect(reverse('users:dashboard'))

        except Exception as exp:
            logging.error(exp)
            print('error is: {}'.format(exp))
            return HttpResponse(exp, status=400)