from django.db import models
from django.urls import reverse

# Create your models here.

WEATHER = (
    ('S', 'Sunny'),
    ('R', 'Rainy'),
    ('C', 'Cloudy'),
    ('W', 'Windy')
)

class Stamp (models.Model):
    country = models.CharField(max_length=100)
    date = models.DateField()
    color = models.CharField(max_length=50)
    shape = models.CharField(max_length=50)

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