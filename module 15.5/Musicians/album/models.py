from django.db import models
from musician.models import Musician
import datetime

# Create your models here.
rate = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]
class Albums(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(default=datetime.date.today())
    rating = models.CharField(max_length=20, choices=rate)

    def __str__(self):
        return self.album_name

