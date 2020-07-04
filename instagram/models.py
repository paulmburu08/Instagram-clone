from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = models.TextField()

    def __str__(self):
        return self.profile_photo

    class Meta:
        ordering = ['profile_photo']

    def save_profile_photo(self):
        self.save()

    def delete_profile_photo(self):
        self.delete()

    @classmethod
    def update_profile_photo(cls,id,profile_photo):
        cls.objects.filter(id = id).update(profile_photo = profile_photo)

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,image):
        cls.objects.filter(id = id).update(image = image)

