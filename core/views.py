from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Book, AudioBook, EBook
from .serializers import BookSerializer, EBookSerializer, AudioBookSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.available()

    def create(self, request, *args, **kwargs):
        title = request.data.get('title')

        if title and Book.objects.filter(title=title).exists():
            return Response({"error": "Book already exists"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)


class EBookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = EBook.objects.all()
    serializer_class = EBookSerializer


class AudioBookViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
