#Source: https://stackoverflow.com/questions/76818922/typeerror-object-of-type-linkpreview-is-not-json-serializable
class PreviewLink(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)
    throttle_scope = 'link_preview'

    def post(self, request):
        serializer = PreviewLinkSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        link = data.get('link')
        user = request.user

        link_preview = user.preview_link(link)

        return Response(link_preview, status=status.HTTP_200_OK)

class LinkIsPreviewable(APIView):
    permission_classes = (IsAuthenticated, IsNotSuspended)
    throttle_scope = 'link_preview'

    def post(self, request):
        serializer = PreviewLinkSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        link = data.get('link')

        try:
            is_previewable = link_preview(url=link)
        except Exception as e:
            is_previewable = False

        return Response({
            'is_previewable': is_previewable
        }, status=status.HTTP_200_OK)