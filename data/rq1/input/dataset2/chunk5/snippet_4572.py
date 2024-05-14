#Source: https://stackoverflow.com/questions/55150153/typeerror-at-myapp-beds
class BedsView(View):
    def get_user_details(self, username, mat_number):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return redirect('index') 
        userbeds = Userbed.objects.filter(user=user, mat_number=mat_number).order_by(-posted_date)[0]
        form = UserBedsForm({'mat_number':userbeds.mat_number})
        return (user, userbeds,form)

    @method_decorator(login_required)
    def get(self, request, username, mat_number):
        (user,userbeds,form) = self.get_user_details(username, mat_number)
        return render(request, 'myapp/beds.html', {'userbeds':userbeds, 'selecteduser':user, 'form':form})

    @method_decorator(login_required)
    def post(self, request, username):
        (user, userbeds, form) = self.get_user_details(username, mat_number)
        form = UserBedsForm(request.POST, instance=userbeds)
        if form.is_valid():
            form.save(commit=True)
            return redirect('beds', user. username)
        else:
            print(form.errors)
        return render(request, 'myapp/beds.html', {'userbeds':userbeds, 'selecteduser':user, 'form':form})