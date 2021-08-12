from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class TagView(viewsets.ModelViewSet):
    """
    viewset for creatig tag 
    tags for easy filtering and categorizing

    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = PageNumberPagination

class NoteView(viewsets.ModelViewSet):
    """
    Viewset for creatig Note
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    pagination_class = PageNumberPagination

