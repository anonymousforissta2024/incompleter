#Source: https://stackoverflow.com/questions/69744733/attributeerror-wsgirequest-object-has-no-attribute-get-heroku
class PostSerializer(serializers.ModelSerializer):
    """Post Serializer"""
    owner = UserProfile(read_only=True)
    tags = TagSerializer(many=True)
    comments = CommentSerializer(many=True, read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'slug',
                  'comments', 'tags', 'description', 'image', 'bookmarks',
                  'created', 'modified', 'blog_views', 'blog_likes',
                  'read_time',)

    def create(self, validated_data):
        """Create a blog post in a customized way."""
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data,
                                   owner=self.context.user)
        for tag in tags:
            tag_qs = Tag.objects.filter(name__iexact=tag.get('name'))
            if tag_qs.exists():
                tag_obj = tag_qs.first()
            else:
                tag_obj = Tag.objects.create(
                    name=tag.get('name'),
                    owner=self.context.user, )
            post.tags.add(tag_obj)

        return post

    def update(self, instance, validated_data):
        """Update blog posts."""
        tags = validated_data.pop('tags', [])
        instance = super(PostSerializer, self).update(instance, validated_data)

        if len(tags):
            for tag in tags:
                tag_qs = Tag.objects.filter(name__iexact=tag.get('name'))
                if tag_qs.exists():
                    tag = tag_qs.first()
                else:
                    tag = Tag.objects.create(name=tag.get('name'),
                                             owner=self.context.user, )
                instance.tags.clear()
                instance.tags.add(tag)

        return instance