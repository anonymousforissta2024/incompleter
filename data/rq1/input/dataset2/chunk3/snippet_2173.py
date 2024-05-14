#Source: https://stackoverflow.com/questions/58761510/typeerror-get-object-takes-1-positional-argument-but-2-were-given
class UserMobileViewSet(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserMobileDevice.objects.all()
    serializer_class = UserMobileSerializer

    def get_user(self, id):
        try:
            UserMobileDevice.objects.get(user=id)
        except User.DoesNotExist:
            return None



    def create(self, request, *args, **kwargs):
        myModel = None
        id = request.data.get("user")  #id = 52 pk = 2
        print(id)
        if id:
            myModel=self.get_user(id)
            print(myModel)
        if myModel:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)