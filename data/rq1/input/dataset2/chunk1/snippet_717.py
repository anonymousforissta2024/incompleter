#Source: https://stackoverflow.com/questions/58683181/django-rest-framework-authentication-permissions-error-typeerror-str-object
from rest_framework import permissions

class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # The method is a safe method
            return True
        else:
            # The method is not a safe method
            # Only owners are granted permissions
            return obj.owner == request.user