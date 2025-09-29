from .models import Book
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Book)
def print_new_book(sender, instance, created, **kwargs):
    if created:
        print(f'New Book Created: {instance}')
