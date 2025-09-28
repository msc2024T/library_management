from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book, AudioBook, EBook
from .serializers import BookSerializer, EBookSerializer, AudioBookSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()

    def get_queryset(self):
        return Book.objects.available()

    serializer_class = BookSerializer


class EBookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = EBook.objects.all()
    serializer_class = EBookSerializer


class AudioBookViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
