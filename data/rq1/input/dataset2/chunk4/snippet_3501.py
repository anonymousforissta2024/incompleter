#Source: https://stackoverflow.com/questions/72217488/django-typeerror-field-id-expected-a-number-but-got-user
@login_required(login_url='login')
def addNote(request):
    notebooks = Notebook.objects.filter(user=request.user)

    if request.method == 'POST':
        data = request.POST
        note = request.POST.get('content')

        if data['notebook'] != 'none':  # 'notebook' é o nome do meu input na minha template
            notebook = Notebook.objects.get(id=data['notebook'])
        elif data['notebook_new'] != '':  # 'notebook_new' é o nome do meu input na minha template
            notebook, created = Notebook.objects.get_or_create(name=data['notebook_new'])  
        else:                                                                      
            notebook = None

        Notes.objects.create(
            notebook=notebook,
            title=data['title_note'],
            content=note,
            user=request.user,
        )

        return redirect('home')

    context = {'notebooks': notebooks}
    return render(request, 'base/add_note.html', context)