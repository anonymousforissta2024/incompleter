#Source: https://stackoverflow.com/questions/69744733/attributeerror-wsgirequest-object-has-no-attribute-get-heroku
class PostDetail(generics.GenericAPIView):
    """Blog post details"""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (PostsProtectOrReadOnly, IsMentorOnly,)
    lookup_field = 'slug'

    def get_post_object(self, slug):
        post = get_blog_by_slug(slug)
        return post

    def get(self, request, slug):
        post = self.get_post_object(slug)
        if not post:
            return response.Response({
                'errors': _('Sorry, Blog post with the specified slug does'
                            'not exist')
            }, status=status.HTTP_404_NOT_FOUND)

        # track views of a viewed blog post.
        ip_address = get_ip_address(request)
        obj = CustomIPAddress.objects.create(address=ip_address)
        post.address_views.add(obj)

        serializer = self.serializer_class(post, context=request)
        return response.Response(serializer.data, status=status.HTTP_200_OK)