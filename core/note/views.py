from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class TagView(viewsets.ModelViewSet):
    """
    viewset for creatig tag 
    tags for easy filtering and categorizing

    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class NoteView(viewsets.ModelViewSet):
    """
    Viewset for creatig Note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

