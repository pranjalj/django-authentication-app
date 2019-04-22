from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#registration form
class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	class Meta:
		model = User
		fields = ['username','first_name','password1','password2']
		widgets = {
			'username': forms.EmailInput(attrs={'placeholder': 'Email'}),#email=username
			'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
			'password1': forms.PasswordInput(),
			'password2': forms.PasswordInput(),
		}
		labels = {
			'username':'Email-id',
			'first_name':'Name',
			'password1':'Password',
			'password2':'Confirm Password',
		}