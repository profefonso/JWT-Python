from django.db import models
from django.utils import timezone


class Detail(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.name
