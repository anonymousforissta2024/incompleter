#Source: https://stackoverflow.com/questions/55509211/how-to-resolve-object-of-type-attributeerror-is-not-json-serializable
class InviteKeyAllCreateView(generics.CreateAPIView):
    """
    POST invitekey/
    """
    serializer_class = InviteKeyCreateAllSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        try:
            # get user count of keys
            cur_key_count = Invite_Key.objects.filter(user_submitter_id=user.id).order_by('-created_at').count()
            if cur_key_count > 0:
                # now we get the latest one
                check_key = Invite_Key.object.filter(user_submitter_id=user.id)[0]
                now = datetime.now()
                if now-timedelta(days=3) <= datetime.datetime.strptime(check_key['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ"):
                    serialized_data = InviteKeyCreateAllSerializer(data=request.data)
                    serialized_data.is_valid(raise_exception=True)
                    serialized_data.save()
                else:
                    return Response(
                        data={
                            "message": "Sorry, you have recently created an Invite Key, try again some other time."
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except Exception as e:
            return Response(
                data={
                    "message": "The Invite Key could not be created.",
                    "error": e
                },
                status=status.HTTP_400_BAD_REQUEST
            )