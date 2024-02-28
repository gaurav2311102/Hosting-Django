from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserPorfileinfo

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ['username','email','password']
        
class UserProfileinfoForm(forms.ModelForm):
    
    class Meta():
        model = UserPorfileinfo
        fields = ['profile_pic','portfolio']