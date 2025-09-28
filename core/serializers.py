from rest_framework import serializers
from .models import Book, EBook, AudioBook


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class EBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = EBook
        fields = '__all__'


class AudioBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioBook
        fields = '__all__'
