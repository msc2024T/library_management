from django.db import models


class BookManager(models.Manager):

    def available(self):

        return self.filter(availability=True)
