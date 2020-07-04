from .models import Profile,Image
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile