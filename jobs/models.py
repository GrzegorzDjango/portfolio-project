from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')  #będą zapisywane w MEDIA_ROOT (setting) /image folderze
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
