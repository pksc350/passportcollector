from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User 

# Create your models here.

WEATHER = (
    ('S', 'Sunny'),
    ('R', 'Rainy'),
    ('C', 'Cloudy'),
    ('W', 'Windy')
)

class Attraction(models.Model):
    title = models.CharField(max_length=100)
    kind = models.CharField(max_length=50)
    # Other goodness such as 'def __str__():' below

    def __str__(self):
        return f'{self.title} {self.kind}'
    # Add this method

    def get_absolute_url(self):
        return reverse('attraction_detail', kwargs={'attraction_id': self.id})

        class Meta:
            ordering = ['-date']



class Stamp (models.Model):
    country = models.CharField(max_length=100)
    date = models.DateField()
    color = models.CharField(max_length=50)
    shape = models.CharField(max_length=50)
    attractions = models.ManyToManyField(Attraction)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.country
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"stamp_id": self.id})


class Weather (models.Model):
    date = models.DateField('Visiting Date')
    weather = models.CharField(max_length=1, choices=WEATHER, default=WEATHER[0][0])
    
    stamp = models.ForeignKey(Stamp, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_weather_display()} on {self.date}'

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    stamp = models.ForeignKey(Stamp, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for stamp_id: {self.stamp_id} @{self.url}'