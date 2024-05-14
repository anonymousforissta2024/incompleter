#Source: https://stackoverflow.com/questions/64882685/typeerror-object-of-type-user-is-not-json-serializable-why-is-this-happening
class UserCreateAPIView(ModelViewSet):
    queryset = EndUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = (AllowAny,)