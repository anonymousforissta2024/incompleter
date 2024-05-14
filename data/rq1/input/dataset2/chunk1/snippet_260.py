#Source: https://stackoverflow.com/questions/47012130/django-attributeerror-nonetype-object-has-no-attribute-method
@permission_classes([UserPermission])
class UserObject(GenericAPIView):

    def get_serializer_class(self):

        if self.request.method == 'POST':
            return ObjectPostSerializer
        return ObjectSerializer

    def post(self, request, user_id):

        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id):

        try:
            object = Object.objects.filter(user=user_id)
        except Object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ObjectSerializer(object, many=True)
        return Response(serializer.data)

    def put(self, request, user_id):

        try:
            object = Object.objects.get(user=user_id)
        except Object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ObjectSerializer(object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):

        try:
            object = Object.objects.filter(user=user_id)
        except Object.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)