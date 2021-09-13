from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput


class CreateUserForm(UserCreationForm):
	password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
	    attrs={'class': 'form-control', 'placeholder': 'New Password'}))
    
	password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
			'email': forms.EmailInput(attrs={'placeholder':'Email'}),
			
        }
