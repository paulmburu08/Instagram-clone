from .models import Profile,Image
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class PostImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes', 'post_date', 'user', 'comments']
        widgets = {
            'name': forms.TextInput()
        }

class Comments(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes', 'post_date', 'user', 'image', 'name', 'caption']
        widgets = {
            'comments': forms.TextInput()
        }