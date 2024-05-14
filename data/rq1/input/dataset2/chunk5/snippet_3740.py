#Source: https://stackoverflow.com/questions/48868516/type-error-with-django-post-method
@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    print(form.errors)
    print(request.POST['task_title'])
    if request.method == 'POST':
        if form.is_valid():
            new_todo = Task(task_title=request.POST['task_title'])
            new_todo.save()
            print('DONE')

    return redirect('index')