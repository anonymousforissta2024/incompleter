#Source: https://stackoverflow.com/questions/57662873/filenotfounderror-winerror-3-the-system-cannot-find-the-path-specified
from rest_framework import routers

from .viewsets import NoteViewSet

router = routers.SimpleRouter()
router.register('notes', NoteViewSet)

urlpatterns = router.urls