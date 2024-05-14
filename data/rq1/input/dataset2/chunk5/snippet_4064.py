#Source: https://stackoverflow.com/questions/53906364/attributeerror-nonetype-object-has-no-attribute-split-sending-post-request
@require_POST
def user_login(request):
    data = json.loads(request.body.decode('utf-8'))
    phone_number = data['phone_number']
    password = data['password']
    user = authenticate(phone_number=phone_number, password=password)
    if user is None:
        message = 'The username or password is wrong.'
        print(message)
        return JsonResponse({'message':message},status=406)
    if not user.two_step_auth:
        login(request,user)
        message='successfully loged in'
        print(message)
        return JsonResponse({'message':message}, status=200)
    gg = generate_activation_code(phone_number)
    if gg:
        message='The Activation code has been sent to your phone'
        print(message)
        return JsonResponse({'message':message}, status=200)
    return JsonResponse({}, status=400)