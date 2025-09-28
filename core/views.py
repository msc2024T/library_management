from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
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

    @action(detail=True, methods=['post'])
    def mark_unavailable(self, request, pk=None):

        try:
            book = Book.objects.get(id=pk)
            book.availability = False
            book.save()
            return Response({'message': 'Book marked as unavailable'}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({'message': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)


class EBookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = EBook.objects.all()
    serializer_class = EBookSerializer


class AudioBookViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
