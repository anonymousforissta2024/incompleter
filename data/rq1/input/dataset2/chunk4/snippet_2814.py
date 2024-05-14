#Source: https://stackoverflow.com/questions/58314475/django-typeerror-listserializer-object-is-not-iterable
class KeyboardEventView(viewsets.ModelViewSet):
    queryset = KeyboardEvent.objects.all()
    serializer_class = KeyboardEventSerializer

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]

            # check if many is required
            if isinstance(data, list):
                kwargs["many"] = True

        return super(KeyboardEventView, self).get_serializer(*args, **kwargs)