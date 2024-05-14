#Source: https://stackoverflow.com/questions/58683181/django-rest-framework-authentication-permissions-error-typeerror-str-object
class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    permission_classes = (
        'permissions.IsAuthenticatedOrReadOnly',
        'custompermission.IsCurrentUserOwnerOrReadOnly',
    )
    filterset_fields = (
        'name',
        'drone_category',
        'manufacturing_date',
        'has_it_competed',
    )
    search_fileds = (
        'name',
    )
    ordering_fields = (
        'name',
        'manufacturing_date',
    )
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'
    permission_classes = (
        'permissions.IsAuthenticatedOrReadOnly',
        'custompermission.IsCurrentUserOwnerOrReadOnly',
    )