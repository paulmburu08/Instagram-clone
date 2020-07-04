from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()

    @receiver(pre_delete, sender=Profile)
    def photo_delete(self, sender, instance, **kwargs):
        cloudinary.uploader.destroy(instance.image.public_id)

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=100)

    @receiver(pre_delete, sender=Image)
    def photo_delete(self, sender, instance, **kwargs):
        cloudinary.uploader.destroy(instance.image.public_id)
