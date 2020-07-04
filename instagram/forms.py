from .models import Profile,Image
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class PostImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes', 'post_date', 'user']