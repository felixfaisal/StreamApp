from django.db import models

# Create your models here.


class VideoInfo(models.Model):
    Video_id = models.IntegerField()
    Video_Name = models.CharField(max_length=200)
    Video_Description = models.CharField(max_length=200)
    Video_Link = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.Video_Name
