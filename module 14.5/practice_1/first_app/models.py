from django.db import models

# Create your models here.
class practice_model(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    birthday = models.DateField()
    date_time = models.DateTimeField()
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')