#Source: https://stackoverflow.com/questions/71877489/typeerror-object-of-type-httpresponseredirect-is-not-json-serializable
class EntryLayerView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        body = request.data
        response = get_endpoint(validated_body) #Don't worry about this line
        return Response(response, status=status.HTTP_200_OK)


class startconversation(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        print("I'm inside the view")
        redirect = request.GET.get('all the data')
        #This is the view I'm trying to pass data to
        