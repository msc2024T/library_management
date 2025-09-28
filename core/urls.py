from .views import BookViewSet, AudioBookViewSet, EBookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('books', BookViewSet)
router.register('ebooks', EBookViewSet)
router.register('audiobooks', AudioBookViewSet)


urlpatterns = [
    path('', include(router.urls))
]
