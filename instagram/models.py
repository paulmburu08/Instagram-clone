from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=60)
    caption = models.TextField()
