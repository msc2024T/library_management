from django.db import models
from .managers import BookManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Book(BaseModel):

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    availability = models.BooleanField(default=True)

    objects = BookManager()


class EBook(Book):

    page_count = models.PositiveIntegerField()
    file_format = models.CharField(max_length=10, choices=[
                                   ('pdf', 'PDF'), ('text', 'TEXT')])


class AudioBook(Book):

    duration = models.DurationField()
    file_format = models.CharField(max_length=10, choices=[
                                   ('mp3', 'MP3'), ('wave', 'WAVE')])


class AvailableBook(Book):

    class Meta:
        proxy = True

    def available_books(self):
        return self.availability == True
