from django.db import models
from django.urls import reverse

# Create your models here.

class Stamp (models.Model):
    country = models.CharField(max_length=100)
    date = models.DateField()
    color = models.CharField(max_length=50)
    shape = models.CharField(max_length=50)

    def __str__(self):
        return self.country
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"stamp_id": self.id})
