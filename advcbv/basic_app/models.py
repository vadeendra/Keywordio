from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})
