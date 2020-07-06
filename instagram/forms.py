from django import forms
from .models import Profile,Image,Comments

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

class AddComments(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image']
        widgets = {
            'comments': forms.TextInput()
        }