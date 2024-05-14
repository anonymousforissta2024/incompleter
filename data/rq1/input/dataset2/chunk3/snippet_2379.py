#Source: https://stackoverflow.com/questions/67347765/attributeerror-after-post-request-in-django
@csrf_exempt
def login(request):
    json_data = json.loads(request.body.decode('utf-8'))
    print(json_data)
    return request.body