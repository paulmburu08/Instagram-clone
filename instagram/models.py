from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.contrib.auth.models import User

# Create your models here.
from tinymce.models import HTMLField
class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio = HTMLField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

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

from tinymce.models import HTMLField
class Image(models.Model):
    image = CloudinaryField('image')
    name = HTMLField()
    caption = HTMLField()
    profile = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    likes = models.IntegerField(default=0)
    comments = HTMLField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

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

