#Source: https://stackoverflow.com/questions/71743807/typeerror-reverse-takes-exactly-2-arguments-1-given
class StartAssessment(generics.GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        data = request.data
        request = build_rp_request(data)
        response = post_to_app_start_assessment(request)
        path = get_path(response)
        step = get_step(response)
        data["path"] = path
        data["step"] = step
        request = build_rp_request(data)
        app_response = post_to_app(request, path)
        message = format_message(app_response)
        return Response(message, status=status.HTTP_200_OK)