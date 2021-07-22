from django.db import models


# Create your models here.
class FilesUpload(models.Model):
    file = models.FileField(upload_to="pictures")


class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150, unique=True)
    profile = models.TextField()

    def __str__(self):
        return self.name
