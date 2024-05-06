from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

    def save(self, commit=True):
        
        user = super().save(commit=False)
        if commit:
            user.save()  
            Profile.objects.create(user=user)
        
        return user
        

class ProfileEdit(forms.Form):
    first = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    about = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    goal = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    pfp = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control'}))
    education = forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))



