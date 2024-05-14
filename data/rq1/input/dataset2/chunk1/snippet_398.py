#Source: https://stackoverflow.com/questions/49809261/attributeerror-type-object-user-has-no-attribute-name
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User