#Source: https://stackoverflow.com/questions/57662873/filenotfounderror-winerror-3-the-system-cannot-find-the-path-specified
from rest_framework import viewsets

from .models import Note
from .serializer import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer