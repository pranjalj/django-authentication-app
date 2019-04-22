from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#registration form
class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Name'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
			'password1': forms.PasswordInput(),
			'password2': forms.PasswordInput(),
		}
		labels = {
			'name':'Name',
			'email':'Email-id',
			'password1':'Password',
			'password2':'Confirm Password',
		}