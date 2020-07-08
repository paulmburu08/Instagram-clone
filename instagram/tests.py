from django.test import TestCase
from .models import Image,Profile,Comments 
# Create your tests here.

class TestProfile(TestCase):

    def setUp(self):
        self.profile = Profile(name = 'Paul',profile_photo = 'image.jpg',bio = 'I am paul')

    def tearDown(self):
        Profile.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.profile.save_profile_photo()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    # Testing delete Method
    def test_delete_method(self):
        self.profile.save_profile_photo()
        self.profile.delete_profile_photo()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    # Testing update Method
    def test_update_method(self):
        self.profile.save_profile_photo()
        self.profile.update_profile_photo(self.name.id,'Ian')
        profiles = Profile.objects.all()
        self.assertTrue(profiles[0].name == 'Ian')

class TestImage(TestCase):

    def setUp(self):
        self.image = Image(image = 'image.jpg', name = 'A tree', caption = 'Awesome tree', post_date = ' 2020-07-08 13:15:54.029897+03 ')

    def tearDown(self):
        Image.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing delete Method
    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    # Testing update Method
    def test_update_method(self):
        self.image.save_image
        self.image.update_image(self.image.id,'image2.jpg')
        images = Image.objects.all()
        self.assertTrue(images[0].image == 'image2.jpg')
