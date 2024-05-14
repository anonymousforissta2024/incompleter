#Source: https://stackoverflow.com/questions/56214565/typeerror-object-of-type-user-is-not-json-serializable
from rest_framework.views import APIView
from rest_framework.response import Response
import json

class MyView(APIView):
    from .serializers import MySerializer
    from app.permissions import MyPermissionClass
    from .models import MyModel

    serializer_class = MySerializer
    queryset = MyModel.objects.all()
    permission_classes = (MyPermissionClass,)
    pagination_class = None

    def get(self, request, *args, **kwargs):
        data=myfunction(a,b,c)
        # data={list}<class 'list'>: [<User: Negiiii | negiiii>, <User: Negiiii | negiiii>]
        data=json.dumps(data)
        return Response({"data":data})