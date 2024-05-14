#Source: https://stackoverflow.com/questions/30953615/typeerror-object-is-not-json-serializable-in-django-1-8-python-3-4
from django.http import HttpRequest,HttpResponse
from django.http import JsonResponse
from json import dumps

def get_stats(request):
    if request.method == "POST":
        srch_dropV = request.POST['srch_dropAJ']
    else:
        srch_dropV = ''
    if(srch_dropV == 'Green'):
        students = GreenBased.objects.all()
    if(srch_dropV == 'Yellow'):
        students = YellowBased.objects.all()
    response_data = {}
    try:
        response_data['result'] = 'Success'
        response_data['message'] = list(students)
    except:
        response_data['result'] = 'Ouch!'
        response_data['message'] = 'Script has not ran correctly'
    return HttpResponse(JsonResponse(response_data), content_type="application/json")