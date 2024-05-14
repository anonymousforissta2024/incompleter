#Source: https://stackoverflow.com/questions/58784123/one-to-one-relationship-how-to-fix-got-attributeerror-when-attempting-to-get-a
class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)