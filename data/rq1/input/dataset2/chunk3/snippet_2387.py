#Source: https://stackoverflow.com/questions/62919896/using-partial-on-drfs-action-gives-typeerror-multiple-values-for-argument
specialised_action = partial(action, methods=["post"], detail=True, url_path="my-action-url")

class SomeViewSet(GenericViewSet):
    @specialised_action
    def action_handler(self, request, *args, **kwargs):
        print("do something")