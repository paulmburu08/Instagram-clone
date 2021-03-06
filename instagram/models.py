from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    name = HTMLField()
    profile_photo = CloudinaryField('image')
    bio = HTMLField()
    followers = models.ManyToManyField(User,related_name='followers')
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.profile_photo

    class Meta:
        ordering = ['profile_photo']

    def save_profile_photo(self):
        self.save()

    def delete_profile_photo(self):
        self.delete()

    def total_followers(self):
        return self.followers.count()

    @classmethod
    def search_by_username(cls,search_term):
        users = cls.objects.filter(user__username__icontains =search_term)
        return users

    @classmethod
    def get_image_by_id(cls,id):
        profile = cls.objects.get(user__id = id)
        return profile

    @classmethod
    def update_profile_photo(cls,id,profile_photo):
        cls.objects.filter(id = id).update(profile_photo = profile_photo)

class Image(models.Model):
    image = CloudinaryField('image')
    name = HTMLField()
    caption = HTMLField()
    likes = models.ManyToManyField(User,related_name='image_post')
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id = id)
        return image

    def total_likes(self):
        return self.likes.count()

    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.get(id = id)
        return images

    @classmethod
    def update_image(cls,id,image):
        cls.objects.filter(id = id).update(image = image)

class Comments(models.Model):
    comments = HTMLField()
    image = models.ForeignKey(Image,on_delete=models.DO_NOTHING)

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id = id)
        return comments
