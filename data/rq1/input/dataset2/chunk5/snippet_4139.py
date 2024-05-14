#Source: https://stackoverflow.com/questions/72492502/nameerror-name-f-is-not-defined
@require_http_methods(["POST"])
def submit_survey(request):
    request.user.give_coins(count=10)
    form_data = request.POST.copy()
    form_items = list(form_data.items())
    print("form_items", form_items)
    form_items.pop(0)  # the first element is the csrf token. Therefore omit it.
    survey = None
    for item in form_items:
        # Here in 'choice/3', '3' is '<choice_id>'.
        choice_str, choice_id = item
        choice_id = int(choice_id.split('/')[1])
        choice = Choice.objects.get(id=choice_id)
        if survey is None:
            survey = choice.question.survey
        choice.votes = choice.votes + 1
        choice.save()
    if survey is not None:
        participant = Participant(survey=survey, participation_datetime=timezone.now())
        participant.save()
    return redirect('/submit_success/')