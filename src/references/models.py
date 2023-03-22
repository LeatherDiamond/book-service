from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class BookAuthor(models.Model):
    name = models.CharField(
       max_length=30,
       verbose_name="Author's name",
    )
    surname = models.CharField(
       max_length=30,
       verbose_name="Author's surname",
    )
    description = models.TextField(
        blank=True,
        null=True
    )
      
    def get_absolute_url(self):
        return reverse_lazy('references:author_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ' ' + self.surname


    